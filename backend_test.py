#!/usr/bin/env python3
"""
Peptide Research Platform - Backend API Testing
Tests all API endpoints using the public URL
"""
import requests
import sys
import json
from datetime import datetime

class PeptideAPITester:
    def __init__(self, base_url="https://peptide-research-15.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None, params=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params, timeout=30)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=30)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    if isinstance(response_data, dict):
                        # Print key info for successful responses
                        if 'peptides' in response_data:
                            print(f"   📊 Found {len(response_data['peptides'])} peptides")
                        elif 'trials' in response_data:
                            print(f"   📊 Found {len(response_data['trials'])} trials")
                        elif 'papers' in response_data:
                            print(f"   📊 Found {len(response_data['papers'])} papers")
                        elif 'news' in response_data:
                            print(f"   📊 Found {len(response_data['news'])} news items")
                        elif 'status' in response_data:
                            print(f"   📊 Status: {response_data['status']}")
                except:
                    pass
            else:
                self.failed_tests.append({
                    'name': name,
                    'expected': expected_status,
                    'actual': response.status_code,
                    'url': url,
                    'response': response.text[:200] if response.text else 'No response'
                })
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"   Response: {response.text[:200]}")

            return success, response.json() if success and response.text else {}

        except Exception as e:
            self.failed_tests.append({
                'name': name,
                'error': str(e),
                'url': url
            })
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_health_check(self):
        """Test health endpoint"""
        return self.run_test("Health Check", "GET", "api/health", 200)

    def test_get_peptides(self):
        """Test get peptides endpoint"""
        return self.run_test("Get Peptides", "GET", "api/peptides", 200)

    def test_get_peptides_with_search(self):
        """Test peptides search"""
        return self.run_test("Search Peptides", "GET", "api/peptides", 200, 
                           params={"query": "semaglutide", "limit": 5})

    def test_get_categories(self):
        """Test get categories"""
        return self.run_test("Get Categories", "GET", "api/peptides/categories", 200)

    def test_get_trials(self):
        """Test get trials endpoint"""
        return self.run_test("Get Trials", "GET", "api/trials", 200, 
                           params={"query": "peptide", "page_size": 10})

    def test_get_trials_with_company(self):
        """Test trials with company filter"""
        return self.run_test("Get Trials (Eli Lilly)", "GET", "api/trials", 200,
                           params={"query": "peptide", "company": "Eli Lilly", "page_size": 5})

    def test_get_papers(self):
        """Test get papers endpoint"""
        return self.run_test("Get Papers", "GET", "api/papers", 200,
                           params={"query": "peptide", "max_results": 10})

    def test_get_papers_sorted(self):
        """Test papers with sorting"""
        return self.run_test("Get Papers (Date Sort)", "GET", "api/papers", 200,
                           params={"query": "peptide therapeutics", "sort": "date", "max_results": 5})

    def test_get_news(self):
        """Test get news endpoint"""
        return self.run_test("Get News", "GET", "api/news", 200,
                           params={"topic": "peptide research", "limit": 10})

    def test_get_stats(self):
        """Test get stats endpoint"""
        return self.run_test("Get Stats", "GET", "api/stats", 200)

    def test_seed_status(self):
        """Test seed status endpoint"""
        return self.run_test("Seed Status", "GET", "api/peptides/seed/status", 200)

    def test_peptide_detail(self):
        """Test peptide detail endpoint - first get a peptide slug"""
        success, peptides_data = self.test_get_peptides()
        if success and peptides_data.get('peptides'):
            slug = peptides_data['peptides'][0].get('slug')
            if slug:
                return self.run_test(f"Get Peptide Detail ({slug})", "GET", f"api/peptides/{slug}", 200)
        
        # Fallback - try common peptide slugs
        common_slugs = ['semaglutide', 'tirzepatide', 'liraglutide', 'oxytocin']
        for slug in common_slugs:
            success, _ = self.run_test(f"Get Peptide Detail ({slug})", "GET", f"api/peptides/{slug}", 200)
            if success:
                return success, _
        
        print("⚠️  No peptides available for detail testing")
        return False, {}

def main():
    print("🧪 Peptide Research Platform - Backend API Testing")
    print("=" * 60)
    
    tester = PeptideAPITester()
    
    # Core API tests
    print("\n📡 Testing Core APIs...")
    tester.test_health_check()
    tester.test_get_stats()
    tester.test_seed_status()
    
    # Peptide endpoints
    print("\n🧬 Testing Peptide APIs...")
    tester.test_get_peptides()
    tester.test_get_peptides_with_search()
    tester.test_get_categories()
    tester.test_peptide_detail()
    
    # External data endpoints
    print("\n🔬 Testing External Data APIs...")
    tester.test_get_trials()
    tester.test_get_trials_with_company()
    tester.test_get_papers()
    tester.test_get_papers_sorted()
    tester.test_get_news()
    
    # Print results
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {tester.tests_passed}/{tester.tests_run} passed")
    
    if tester.failed_tests:
        print(f"\n❌ Failed Tests ({len(tester.failed_tests)}):")
        for i, test in enumerate(tester.failed_tests, 1):
            print(f"{i}. {test['name']}")
            if 'error' in test:
                print(f"   Error: {test['error']}")
            else:
                print(f"   Expected: {test['expected']}, Got: {test['actual']}")
            print(f"   URL: {test['url']}")
            if 'response' in test:
                print(f"   Response: {test['response']}")
    
    success_rate = (tester.tests_passed / tester.tests_run) * 100 if tester.tests_run > 0 else 0
    print(f"\n🎯 Success Rate: {success_rate:.1f}%")
    
    if success_rate >= 80:
        print("✅ Backend APIs are working well!")
        return 0
    elif success_rate >= 50:
        print("⚠️  Backend APIs have some issues but core functionality works")
        return 1
    else:
        print("❌ Backend APIs have major issues")
        return 2

if __name__ == "__main__":
    sys.exit(main())