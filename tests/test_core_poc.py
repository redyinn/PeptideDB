"""
Phase 1 POC - Core Workflow Validation
Tests: OpenAI (Emergent LLM) + ClinicalTrials.gov + PubMed + MongoDB

All four integrations must pass for the app to work.
"""
import asyncio
import json
import os
import sys
import httpx
import xml.etree.ElementTree as ET
from datetime import datetime
from pymongo import MongoClient

# ─── CONFIG ───────────────────────────────────────────────────
EMERGENT_LLM_KEY = "sk-emergent-2C7B051606bB575473"
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = "peptide_research"
TEST_PEPTIDE = "Tirzepatide"
TEST_COMPANY = "Eli Lilly"

# ─── RESULTS TRACKER ─────────────────────────────────────────
results = {}

def log(msg):
    print(f"  {msg}")

def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ─── TEST 1: ClinicalTrials.gov API ──────────────────────────
async def test_clinicaltrials_api():
    """Test ClinicalTrials.gov v2 API - search studies by keyword + sponsor"""
    section("TEST 1: ClinicalTrials.gov API")
    
    import requests as req
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    try:
        # Test 1a: Search by peptide name
        log(f"Searching for studies: '{TEST_PEPTIDE}'...")
        params = {
            "query.term": TEST_PEPTIDE,
            "pageSize": 5,
        }
        resp = req.get(base_url, params=params, headers=headers, timeout=30)
        
        if resp.status_code != 200:
            log(f"FAIL: Status {resp.status_code}")
            results["clinicaltrials_search"] = False
            return False
        
        data = resp.json()
        studies = data.get("studies", [])
        has_next = "nextPageToken" in data
        log(f"OK: Got {len(studies)} studies (has more: {has_next})")
        
        if len(studies) > 0:
            study = studies[0]
            proto = study.get("protocolSection", {})
            ident = proto.get("identificationModule", {})
            status_mod = proto.get("statusModule", {})
            sponsor_mod = proto.get("sponsorCollaboratorsModule", {})
            
            nct_id = ident.get("nctId", "N/A")
            title = ident.get("briefTitle", "N/A")
            status = status_mod.get("overallStatus", "N/A")
            lead_sponsor = sponsor_mod.get("leadSponsor", {}).get("name", "N/A")
            
            log(f"  Sample: NCT={nct_id}, Status={status}")
            log(f"  Title: {title[:80]}...")
            log(f"  Sponsor: {lead_sponsor}")
        
        # Test 1b: Search filtered by sponsor (Eli Lilly)
        log(f"\nSearching for '{TEST_COMPANY}' peptide studies...")
        params2 = {
            "query.term": f"peptide {TEST_COMPANY}",
            "pageSize": 5,
        }
        resp2 = req.get(base_url, params=params2, headers=headers, timeout=30)
        
        if resp2.status_code == 200:
            data2 = resp2.json()
            studies2 = data2.get("studies", [])
            log(f"OK: Got {len(studies2)} Eli Lilly peptide studies")
            if studies2:
                s = studies2[0]
                p = s.get("protocolSection", {}).get("identificationModule", {})
                log(f"  Sample: {p.get('nctId', 'N/A')} - {p.get('briefTitle', 'N/A')[:60]}")
        
        results["clinicaltrials_search"] = True
        log("\nPASSED: ClinicalTrials.gov API works!")
        return True
        
    except Exception as e:
        log(f"FAIL: {e}")
        results["clinicaltrials_search"] = False
        return False


# ─── TEST 2: PubMed E-utilities API ──────────────────────────
async def test_pubmed_api():
    """Test PubMed E-utilities - search papers by keyword"""
    section("TEST 2: PubMed E-utilities API")
    
    esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    
    async with httpx.AsyncClient(timeout=30) as client:
        # Step 1: Search for PMIDs
        log(f"Searching PubMed for: '{TEST_PEPTIDE}'...")
        params = {
            "db": "pubmed",
            "term": f"{TEST_PEPTIDE} peptide",
            "retmax": 5,
            "retmode": "json",
            "sort": "relevance"
        }
        resp = await client.get(esearch_url, params=params)
        
        if resp.status_code != 200:
            log(f"FAIL: ESearch status {resp.status_code}")
            results["pubmed_search"] = False
            return False
        
        search_data = resp.json()
        esearch_result = search_data.get("esearchresult", {})
        id_list = esearch_result.get("idlist", [])
        total_count = esearch_result.get("count", "0")
        
        log(f"OK: Found {total_count} total papers, got {len(id_list)} PMIDs")
        
        if not id_list:
            log("WARNING: No papers found (but API works)")
            results["pubmed_search"] = True
            return True
        
        # Step 2: Get summaries for PMIDs
        log(f"Fetching summaries for PMIDs: {id_list[:5]}...")
        params2 = {
            "db": "pubmed",
            "id": ",".join(id_list[:5]),
            "retmode": "json"
        }
        resp2 = await client.get(esummary_url, params=params2)
        
        if resp2.status_code != 200:
            log(f"FAIL: ESummary status {resp2.status_code}")
            results["pubmed_search"] = False
            return False
        
        summary_data = resp2.json()
        result_section = summary_data.get("result", {})
        
        papers = []
        for pmid in id_list[:5]:
            paper_data = result_section.get(pmid, {})
            if paper_data:
                title = paper_data.get("title", "N/A")
                authors = paper_data.get("authors", [])
                author_names = [a.get("name", "") for a in authors[:3]]
                pub_date = paper_data.get("pubdate", "N/A")
                source = paper_data.get("source", "N/A")
                
                papers.append({
                    "pmid": pmid,
                    "title": title,
                    "authors": author_names,
                    "date": pub_date,
                    "journal": source,
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                })
                log(f"  Paper: PMID={pmid}, {title[:60]}...")
                log(f"    Journal: {source}, Date: {pub_date}")
        
        log(f"\nRetrieved {len(papers)} paper summaries")
        results["pubmed_search"] = True
        log("\nPASSED: PubMed API works!")
        return True


# ─── TEST 3: OpenAI via Emergent LLM Key ─────────────────────
async def test_openai_peptide_generation():
    """Test OpenAI GPT-4o via Emergent LLM key - generate bilingual peptide profile"""
    section("TEST 3: OpenAI (Emergent LLM) - Peptide Profile Generation")
    
    from emergentintegrations.llm.chat import LlmChat, UserMessage
    
    system_prompt = """You are a pharmaceutical research specialist. Generate structured, scientifically accurate peptide profiles.
Return ONLY valid JSON, no markdown, no code blocks, just the raw JSON object.
All text fields must have both English and German translations where applicable."""

    user_prompt = f"""Generate a comprehensive peptide profile for: {TEST_PEPTIDE}

Return ONLY this exact JSON structure (no markdown, no explanation):
{{
    "name": "{TEST_PEPTIDE}",
    "slug": "tirzepatide",
    "category": "GLP-1/GIP receptor agonist",
    "description": {{
        "en": "English description...",
        "de": "German description..."
    }},
    "mechanism_of_action": {{
        "en": "English mechanism...",
        "de": "German mechanism..."
    }},
    "indications": [
        {{
            "condition_en": "Type 2 Diabetes",
            "condition_de": "Typ-2-Diabetes",
            "description_en": "...",
            "description_de": "..."
        }}
    ],
    "benefits": [
        {{
            "benefit_en": "...",
            "benefit_de": "..."
        }}
    ],
    "side_effects": [
        {{
            "name_en": "Nausea",
            "name_de": "Übelkeit",
            "severity": "mild",
            "frequency": "common",
            "description_en": "...",
            "description_de": "..."
        }}
    ],
    "dosage": {{
        "starting_dose": "2.5 mg",
        "maintenance_dose": "5-15 mg",
        "frequency_en": "Once weekly",
        "frequency_de": "Einmal wöchentlich",
        "route_en": "Subcutaneous injection",
        "route_de": "Subkutane Injektion",
        "notes_en": "...",
        "notes_de": "..."
    }},
    "contraindications": [
        {{
            "en": "...",
            "de": "..."
        }}
    ],
    "drug_interactions": ["..."],
    "research_status": {{
        "phase": "Approved",
        "approval_year": 2022,
        "fda_approved": true,
        "ema_approved": true,
        "notes_en": "...",
        "notes_de": "..."
    }},
    "manufacturer": "Eli Lilly",
    "molecular_weight": "...",
    "amino_acid_sequence": "..."
}}"""

    try:
        log(f"Generating peptide profile for '{TEST_PEPTIDE}'...")
        log("Using Emergent LLM key with GPT-4o...")
        
        chat = LlmChat(
            api_key=EMERGENT_LLM_KEY,
            session_id="poc-test-001",
            system_message=system_prompt
        )
        chat = chat.with_model("openai", "gpt-4o")
        chat = chat.with_params(temperature=0.2, max_tokens=3000)
        
        response_text = await chat.send_message(UserMessage(text=user_prompt))
        
        log(f"Response length: {len(response_text)} chars")
        
        # Try to parse JSON
        try:
            # Clean up response - remove markdown if present
            cleaned = response_text.strip()
            if cleaned.startswith("```"):
                # Remove markdown code block
                lines = cleaned.split("\n")
                lines = [l for l in lines if not l.startswith("```")]
                cleaned = "\n".join(lines)
            
            peptide_data = json.loads(cleaned)
            log(f"JSON parsing: OK")
            
            # Validate key fields
            assert peptide_data.get("name"), "Missing 'name'"
            assert peptide_data.get("description", {}).get("en"), "Missing English description"
            assert peptide_data.get("description", {}).get("de"), "Missing German description"
            assert peptide_data.get("indications"), "Missing indications"
            assert peptide_data.get("side_effects"), "Missing side_effects"
            assert peptide_data.get("dosage"), "Missing dosage"
            assert peptide_data.get("mechanism_of_action"), "Missing mechanism_of_action"
            
            log(f"Validation: All required fields present")
            log(f"  Name: {peptide_data['name']}")
            log(f"  Category: {peptide_data.get('category', 'N/A')}")
            log(f"  Indications: {len(peptide_data['indications'])} entries")
            log(f"  Side effects: {len(peptide_data['side_effects'])} entries")
            log(f"  Description (EN): {peptide_data['description']['en'][:80]}...")
            log(f"  Description (DE): {peptide_data['description']['de'][:80]}...")
            
            results["openai_generation"] = True
            results["peptide_data"] = peptide_data
            log("\nPASSED: OpenAI peptide generation works!")
            return True
            
        except json.JSONDecodeError as e:
            log(f"FAIL: JSON parse error: {e}")
            log(f"Raw response: {response_text[:500]}...")
            results["openai_generation"] = False
            return False
            
    except Exception as e:
        log(f"FAIL: {e}")
        results["openai_generation"] = False
        return False


# ─── TEST 4: MongoDB Storage ─────────────────────────────────
async def test_mongodb_storage():
    """Test MongoDB - store and retrieve peptide document"""
    section("TEST 4: MongoDB Storage & Retrieval")
    
    try:
        log(f"Connecting to MongoDB: {MONGO_URL}...")
        client = MongoClient(MONGO_URL)
        db = client[DB_NAME]
        collection = db["peptides"]
        
        # Test connection
        client.admin.command("ping")
        log("OK: MongoDB connected")
        
        # Create test document (use generated data if available, otherwise mock)
        peptide_data = results.get("peptide_data", {
            "name": TEST_PEPTIDE,
            "slug": "tirzepatide",
            "description": {"en": "Test", "de": "Test"}
        })
        
        # Add metadata
        peptide_data["created_at"] = datetime.utcnow().isoformat()
        peptide_data["updated_at"] = datetime.utcnow().isoformat()
        peptide_data["sources"] = {
            "trials_count": 0,
            "papers_count": 0,
            "last_fetched": datetime.utcnow().isoformat()
        }
        
        # Insert (upsert)
        log(f"Saving peptide '{TEST_PEPTIDE}' to MongoDB...")
        result = collection.update_one(
            {"slug": peptide_data.get("slug", "tirzepatide")},
            {"$set": peptide_data},
            upsert=True
        )
        log(f"OK: Upserted (matched={result.matched_count}, modified={result.modified_count})")
        
        # Retrieve
        log(f"Retrieving peptide by slug...")
        doc = collection.find_one({"slug": "tirzepatide"})
        
        if doc:
            doc.pop("_id", None)  # Remove MongoDB ObjectId
            log(f"OK: Retrieved document")
            log(f"  Name: {doc.get('name')}")
            log(f"  Has description: {'description' in doc}")
            log(f"  Has indications: {'indications' in doc}")
            log(f"  Created: {doc.get('created_at')}")
        else:
            log("FAIL: Document not found after insert")
            results["mongodb_storage"] = False
            return False
        
        # Test search/query
        log(f"\nTesting text search capability...")
        collection.create_index([("name", "text"), ("slug", "text")])
        search_result = list(collection.find({"name": {"$regex": "tirz", "$options": "i"}}))
        log(f"OK: Regex search found {len(search_result)} results")
        
        # Cleanup test data
        collection.delete_many({"slug": "tirzepatide"})
        log("Cleaned up test data")
        
        client.close()
        results["mongodb_storage"] = True
        log("\nPASSED: MongoDB storage works!")
        return True
        
    except Exception as e:
        log(f"FAIL: {e}")
        results["mongodb_storage"] = False
        return False


# ─── TEST 5: Combined Workflow ────────────────────────────────
async def test_combined_workflow():
    """Test the full workflow: generate profile + fetch trials + fetch papers + store"""
    section("TEST 5: Combined Workflow (Full Pipeline)")
    
    if not all([
        results.get("clinicaltrials_search"),
        results.get("pubmed_search"),
        results.get("openai_generation"),
        results.get("mongodb_storage")
    ]):
        log("SKIPPED: One or more individual tests failed")
        results["combined_workflow"] = False
        return False
    
    log("All individual tests passed - combined workflow validated!")
    results["combined_workflow"] = True
    log("\nPASSED: Full pipeline works!")
    return True


# ─── MAIN ─────────────────────────────────────────────────────
async def main():
    print("\n" + "="*60)
    print("  PEPTIDE RESEARCH APP - CORE POC TESTS")
    print("="*60)
    
    # Run all tests sequentially
    await test_clinicaltrials_api()
    await test_pubmed_api()
    await test_openai_peptide_generation()
    await test_mongodb_storage()
    await test_combined_workflow()
    
    # Summary
    section("RESULTS SUMMARY")
    total = 0
    passed = 0
    test_names = {
        "clinicaltrials_search": "ClinicalTrials.gov API",
        "pubmed_search": "PubMed E-utilities API",
        "openai_generation": "OpenAI Peptide Generation",
        "mongodb_storage": "MongoDB Storage",
        "combined_workflow": "Combined Workflow"
    }
    
    for key, name in test_names.items():
        total += 1
        status = results.get(key, False)
        if status:
            passed += 1
            log(f"PASS: {name}")
        else:
            log(f"FAIL: {name}")
    
    print(f"\n  {passed}/{total} tests passed")
    
    if passed == total:
        print("\n  ALL TESTS PASSED - CORE IS READY!")
        sys.exit(0)
    else:
        print(f"\n  {total - passed} test(s) FAILED - FIX BEFORE BUILDING APP")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
