"""
Peptide Research Platform - Backend API
FastAPI server with MongoDB, ClinicalTrials.gov, PubMed, and OpenAI integrations
"""
import os
import json
import re
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Optional, List
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()

import requests as http_requests
from fastapi import FastAPI, HTTPException, Query, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pymongo import MongoClient, ASCENDING, TEXT
from bson import ObjectId

# ─── CONFIG ──────────────────────────────────────────────────
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DB_NAME", "peptide_research")
EMERGENT_LLM_KEY = os.environ.get("EMERGENT_LLM_KEY", "")
CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ─── MONGODB ─────────────────────────────────────────────────
client = MongoClient(MONGO_URL)
db = client[DB_NAME]
peptides_col = db["peptides"]
trials_cache_col = db["trials_cache"]
papers_cache_col = db["papers_cache"]
news_cache_col = db["news_cache"]

# Create indexes
peptides_col.create_index([("slug", ASCENDING)], unique=True)
peptides_col.create_index([("name", TEXT), ("category", TEXT)])
trials_cache_col.create_index([("query", ASCENDING)])
papers_cache_col.create_index([("query", ASCENDING)])

# ─── HELPERS ─────────────────────────────────────────────────
def serialize_doc(doc):
    """Convert MongoDB document to JSON-serializable dict"""
    if doc is None:
        return None
    doc = dict(doc)
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    for key, val in doc.items():
        if isinstance(val, datetime):
            doc[key] = val.isoformat()
        elif isinstance(val, ObjectId):
            doc[key] = str(val)
    return doc

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text

CT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Accept": "application/json"
}

# ─── PYDANTIC MODELS ─────────────────────────────────────────
class PeptideGenerateRequest(BaseModel):
    name: str
    force_refresh: bool = False

class PeptideSearchQuery(BaseModel):
    query: str = ""
    category: str = ""
    page: int = 1
    limit: int = 20

# ─── CLINICAL TRIALS.GOV ─────────────────────────────────────
def fetch_clinical_trials(query: str, company: str = "", status: str = "", page_size: int = 20):
    """Fetch clinical trials from ClinicalTrials.gov v2 API"""
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    
    search_term = query
    if company:
        search_term = f"{query} {company}"
    
    params = {
        "query.term": search_term,
        "pageSize": min(page_size, 50),
    }
    
    if status:
        status_map = {
            "recruiting": "RECRUITING",
            "completed": "COMPLETED",
            "active": "ACTIVE_NOT_RECRUITING",
            "not_yet": "NOT_YET_RECRUITING",
            "terminated": "TERMINATED",
            "withdrawn": "WITHDRAWN",
        }
        mapped = status_map.get(status.lower(), status.upper())
        params["filter.overallStatus"] = mapped
    
    try:
        resp = http_requests.get(base_url, params=params, headers=CT_HEADERS, timeout=20)
        if resp.status_code != 200:
            logger.error(f"ClinicalTrials API error: {resp.status_code}")
            return []
        
        data = resp.json()
        studies = data.get("studies", [])
        
        results = []
        for study in studies:
            proto = study.get("protocolSection", {})
            ident = proto.get("identificationModule", {})
            status_mod = proto.get("statusModule", {})
            sponsor_mod = proto.get("sponsorCollaboratorsModule", {})
            design_mod = proto.get("designModule", {})
            conditions_mod = proto.get("conditionsModule", {})
            desc_mod = proto.get("descriptionModule", {})
            
            nct_id = ident.get("nctId", "")
            phases = design_mod.get("phases", [])
            
            results.append({
                "nct_id": nct_id,
                "title": ident.get("briefTitle", ""),
                "official_title": ident.get("officialTitle", ""),
                "status": status_mod.get("overallStatus", ""),
                "start_date": status_mod.get("startDateStruct", {}).get("date", ""),
                "completion_date": status_mod.get("completionDateStruct", {}).get("date", ""),
                "phase": ", ".join(phases) if phases else "N/A",
                "sponsor": sponsor_mod.get("leadSponsor", {}).get("name", ""),
                "sponsor_type": sponsor_mod.get("leadSponsor", {}).get("class", ""),
                "conditions": conditions_mod.get("conditions", []),
                "brief_summary": desc_mod.get("briefSummary", ""),
                "url": f"https://clinicaltrials.gov/study/{nct_id}",
                "last_updated": status_mod.get("lastUpdateSubmitDate", ""),
            })
        
        return results
    except Exception as e:
        logger.error(f"ClinicalTrials fetch error: {e}")
        return []

# ─── PUBMED ──────────────────────────────────────────────────
def fetch_pubmed_papers(query: str, max_results: int = 20, sort: str = "relevance"):
    """Fetch papers from PubMed E-utilities"""
    esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    
    try:
        # Step 1: Search for PMIDs
        sort_param = "relevance" if sort == "relevance" else "pub_date"
        params = {
            "db": "pubmed",
            "term": f"{query} peptide",
            "retmax": min(max_results, 50),
            "retmode": "json",
            "sort": sort_param
        }
        resp = http_requests.get(esearch_url, params=params, timeout=15)
        if resp.status_code != 200:
            return [], 0
        
        search_data = resp.json()
        esearch_result = search_data.get("esearchresult", {})
        id_list = esearch_result.get("idlist", [])
        total_count = int(esearch_result.get("count", "0"))
        
        if not id_list:
            return [], total_count
        
        # Step 2: Get summaries
        params2 = {
            "db": "pubmed",
            "id": ",".join(id_list),
            "retmode": "json"
        }
        resp2 = http_requests.get(esummary_url, params=params2, timeout=15)
        if resp2.status_code != 200:
            return [], total_count
        
        summary_data = resp2.json()
        result_section = summary_data.get("result", {})
        
        papers = []
        for pmid in id_list:
            paper = result_section.get(pmid, {})
            if not paper or isinstance(paper, str):
                continue
            
            authors = paper.get("authors", [])
            author_names = [a.get("name", "") for a in authors[:5]]
            
            papers.append({
                "pmid": pmid,
                "title": paper.get("title", ""),
                "authors": author_names,
                "journal": paper.get("source", ""),
                "pub_date": paper.get("pubdate", ""),
                "volume": paper.get("volume", ""),
                "issue": paper.get("issue", ""),
                "pages": paper.get("pages", ""),
                "doi": paper.get("elocationid", ""),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "abstract_available": bool(paper.get("hasabstract")),
            })
        
        return papers, total_count
    except Exception as e:
        logger.error(f"PubMed fetch error: {e}")
        return [], 0

# ─── OPENAI PEPTIDE GENERATION ───────────────────────────────
async def generate_peptide_profile(peptide_name: str):
    """Generate comprehensive bilingual peptide profile using OpenAI"""
    from emergentintegrations.llm.chat import LlmChat, UserMessage
    
    system_prompt = """You are a pharmaceutical research specialist. Generate scientifically accurate peptide profiles.
Return ONLY valid JSON, no markdown, no code blocks, just the raw JSON object.
All text fields must have both English (en) and German (de) translations."""

    user_prompt = f"""Generate a comprehensive peptide profile for: {peptide_name}

Return ONLY this exact JSON structure:
{{
    "name": "{peptide_name}",
    "slug": "{slugify(peptide_name)}",
    "category": "category name",
    "description": {{
        "en": "Detailed English description (3-4 sentences)",
        "de": "Detaillierte deutsche Beschreibung (3-4 Sätze)"
    }},
    "mechanism_of_action": {{
        "en": "Detailed mechanism of action explanation",
        "de": "Detaillierte Erklärung des Wirkmechanismus"
    }},
    "indications": [
        {{
            "condition_en": "Condition name in English",
            "condition_de": "Indikation auf Deutsch",
            "description_en": "Description of indication",
            "description_de": "Beschreibung der Indikation"
        }}
    ],
    "benefits": [
        {{
            "benefit_en": "Benefit in English",
            "benefit_de": "Nutzen auf Deutsch"
        }}
    ],
    "side_effects": [
        {{
            "name_en": "Side effect name English",
            "name_de": "Nebenwirkung auf Deutsch",
            "severity": "mild|moderate|severe",
            "frequency": "common|uncommon|rare",
            "description_en": "Description",
            "description_de": "Beschreibung"
        }}
    ],
    "dosage": {{
        "starting_dose": "dose",
        "maintenance_dose": "dose range",
        "frequency_en": "Frequency in English",
        "frequency_de": "Häufigkeit auf Deutsch",
        "route_en": "Route of administration",
        "route_de": "Verabreichungsweg",
        "notes_en": "Additional notes",
        "notes_de": "Zusätzliche Hinweise"
    }},
    "contraindications": [
        {{
            "en": "Contraindication in English",
            "de": "Kontraindikation auf Deutsch"
        }}
    ],
    "drug_interactions": ["interaction 1", "interaction 2"],
    "research_status": {{
        "phase": "Phase or Approved",
        "fda_approved": true,
        "ema_approved": true,
        "notes_en": "Status notes English",
        "notes_de": "Statusnotizen Deutsch"
    }},
    "manufacturer": "Manufacturer name",
    "molecular_weight": "weight in Da",
    "amino_acid_count": "number",
    "half_life": "duration",
    "storage_conditions": {{
        "en": "Storage conditions",
        "de": "Lagerbedingungen"
    }},
    "amino_acid_sequence": "Full amino acid sequence in one-letter code (e.g. HAEGTFTSDVSSYLEG...) or 'Synthetic small molecule' if not a peptide chain",
    "reconstitution_info": {{
        "preparation_en": "Reconstitution instructions in English",
        "preparation_de": "Rekonstitutionsanleitung auf Deutsch",
        "storage_temperature": "2-8°C",
        "shelf_life_unopened": "e.g. 24 months",
        "shelf_life_reconstituted": "e.g. 28 days refrigerated",
        "light_sensitive": true,
        "solvent": "e.g. Bacteriostatic water, 0.9% NaCl"
    }},
    "application_goals": [
        {{
            "goal_en": "e.g. Fat Loss, Muscle Building, Healing, Anti-Aging, Cognitive Enhancement, Immune Support",
            "goal_de": "e.g. Fettverbrennung, Muskelaufbau, Heilung, Anti-Aging, Kognitive Verbesserung, Immununterstützung",
            "relevance": "primary|secondary"
        }}
    ]
}}

Include at least 3 indications, 4 benefits, 5 side effects, and 3 contraindications.
Include at least 2 application_goals with relevance levels.
Provide a real amino acid sequence if known, or a representative sequence for synthetic peptides.
Make all information scientifically accurate and detailed."""

    try:
        chat = LlmChat(
            api_key=EMERGENT_LLM_KEY,
            session_id=f"peptide-gen-{slugify(peptide_name)}",
            system_message=system_prompt
        )
        chat = chat.with_model("openai", "gpt-4o")
        chat = chat.with_params(temperature=0.2, max_tokens=4000)
        
        response_text = await chat.send_message(UserMessage(text=user_prompt))
        
        # Parse JSON
        cleaned = response_text.strip()
        if cleaned.startswith("```"):
            lines = cleaned.split("\n")
            lines = [l for l in lines if not l.startswith("```")]
            cleaned = "\n".join(lines)
        
        peptide_data = json.loads(cleaned)
        peptide_data["created_at"] = datetime.utcnow().isoformat()
        peptide_data["updated_at"] = datetime.utcnow().isoformat()
        peptide_data["generated_by"] = "gpt-4o"
        
        return peptide_data
    except Exception as e:
        logger.error(f"Peptide generation error: {e}")
        raise

# ─── SEED DATA ───────────────────────────────────────────────
IMPORTANT_PEPTIDES = [
    "Tirzepatide", "Semaglutide", "Liraglutide", "Dulaglutide",
    "Oxytocin", "Insulin", "BPC-157", "TB-500",
    "GHK-Cu", "Ipamorelin", "CJC-1295", "Sermorelin",
    "Melanotan II", "PT-141", "AOD-9604", "Epitalon",
    "Thymosin Alpha 1", "LL-37", "Kisspeptin", "Retatrutide"
]

# ─── FASTAPI APP ─────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Peptide Research Platform starting...")
    yield
    logger.info("Shutting down...")

app = FastAPI(title="Peptide Research Platform API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── API ENDPOINTS ───────────────────────────────────────────

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

# ─── PEPTIDES ────────────────────────────────────────────────

@app.get("/api/peptides")
async def get_peptides(
    query: str = "",
    category: str = "",
    goal: str = "",
    page: int = 1,
    limit: int = 20
):
    """Get all peptides with optional search/filter"""
    filter_q = {}
    if query:
        filter_q["$or"] = [
            {"name": {"$regex": query, "$options": "i"}},
            {"category": {"$regex": query, "$options": "i"}},
            {"slug": {"$regex": query, "$options": "i"}},
        ]
    if category:
        filter_q["category"] = {"$regex": category, "$options": "i"}
    if goal:
        filter_q["application_goals.goal_en"] = {"$regex": goal, "$options": "i"}
    
    skip = (page - 1) * limit
    total = peptides_col.count_documents(filter_q)
    docs = list(peptides_col.find(filter_q).sort("name", 1).skip(skip).limit(limit))
    
    return {
        "peptides": [serialize_doc(d) for d in docs],
        "total": total,
        "page": page,
        "pages": max(1, (total + limit - 1) // limit)
    }

@app.get("/api/peptides/compare")
async def compare_peptides(slugs: str = ""):
    """Compare two peptides side by side"""
    slug_list = [s.strip() for s in slugs.split(",") if s.strip()]
    if len(slug_list) < 2:
        raise HTTPException(status_code=400, detail="Provide at least 2 slugs separated by commas")
    if len(slug_list) > 3:
        slug_list = slug_list[:3]

    results = []
    for slug in slug_list:
        doc = peptides_col.find_one({"slug": slug})
        if doc:
            results.append(serialize_doc(doc))

    if len(results) < 2:
        raise HTTPException(status_code=404, detail="Could not find enough peptides to compare")

    return {"peptides": results, "count": len(results)}

@app.get("/api/peptides/categories")
async def get_peptide_categories():
    """Get distinct peptide categories"""
    categories = peptides_col.distinct("category")
    return {"categories": [c for c in categories if c]}

@app.get("/api/peptides/{slug}")
async def get_peptide_detail(slug: str):
    """Get detailed peptide information by slug"""
    doc = peptides_col.find_one({"slug": slug})
    if not doc:
        raise HTTPException(status_code=404, detail="Peptide not found")
    return serialize_doc(doc)

@app.post("/api/peptides/generate")
async def generate_peptide(req: PeptideGenerateRequest):
    """Generate a peptide profile using AI"""
    existing = peptides_col.find_one({"slug": slugify(req.name)})
    if existing and not req.force_refresh:
        return serialize_doc(existing)
    
    try:
        profile = await generate_peptide_profile(req.name)
        profile["slug"] = slugify(req.name)
        
        peptides_col.update_one(
            {"slug": profile["slug"]},
            {"$set": profile},
            upsert=True
        )
        
        doc = peptides_col.find_one({"slug": profile["slug"]})
        return serialize_doc(doc)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/peptides/seed")
async def seed_peptides(background_tasks: BackgroundTasks):
    """Seed the database with important peptides"""
    existing = peptides_col.count_documents({})
    if existing >= 10:
        return {"message": f"Database already has {existing} peptides", "count": existing}
    
    async def seed_task():
        for name in IMPORTANT_PEPTIDES:
            slug = slugify(name)
            if not peptides_col.find_one({"slug": slug}):
                try:
                    profile = await generate_peptide_profile(name)
                    profile["slug"] = slug
                    peptides_col.update_one(
                        {"slug": slug},
                        {"$set": profile},
                        upsert=True
                    )
                    logger.info(f"Seeded: {name}")
                    await asyncio.sleep(1)
                except Exception as e:
                    logger.error(f"Failed to seed {name}: {e}")
    
    background_tasks.add_task(seed_task)
    return {"message": "Seeding started in background", "peptides": IMPORTANT_PEPTIDES}

@app.get("/api/peptides/seed/status")
async def seed_status():
    """Check how many peptides are seeded"""
    count = peptides_col.count_documents({})
    return {
        "seeded": count,
        "total_expected": len(IMPORTANT_PEPTIDES),
        "complete": count >= len(IMPORTANT_PEPTIDES),
        "peptides": list(peptides_col.find({}, {"name": 1, "slug": 1, "_id": 0}))
    }

# ─── CLINICAL TRIALS ─────────────────────────────────────────

@app.get("/api/trials")
async def get_trials(
    query: str = "peptide",
    company: str = "",
    status: str = "",
    page_size: int = 20
):
    """Fetch clinical trials from ClinicalTrials.gov"""
    cache_key = f"{query}_{company}_{status}"
    
    # Check cache (1 hour)
    cached = trials_cache_col.find_one({"query": cache_key})
    if cached:
        cached_time = datetime.fromisoformat(cached.get("cached_at", "2000-01-01"))
        if datetime.utcnow() - cached_time < timedelta(hours=1):
            return {
                "trials": cached.get("trials", []),
                "total": len(cached.get("trials", [])),
                "cached": True,
                "query": query,
                "company": company,
                "status": status
            }
    
    trials = fetch_clinical_trials(query, company, status, page_size)
    
    # Cache results
    trials_cache_col.update_one(
        {"query": cache_key},
        {"$set": {"trials": trials, "cached_at": datetime.utcnow().isoformat(), "query": cache_key}},
        upsert=True
    )
    
    return {
        "trials": trials,
        "total": len(trials),
        "cached": False,
        "query": query,
        "company": company,
        "status": status
    }

# ─── PAPERS ──────────────────────────────────────────────────

@app.get("/api/papers")
async def get_papers(
    query: str = "peptide",
    sort: str = "relevance",
    max_results: int = 20
):
    """Fetch papers from PubMed"""
    cache_key = f"{query}_{sort}_{max_results}"
    
    # Check cache (1 hour)
    cached = papers_cache_col.find_one({"query": cache_key})
    if cached:
        cached_time = datetime.fromisoformat(cached.get("cached_at", "2000-01-01"))
        if datetime.utcnow() - cached_time < timedelta(hours=1):
            return {
                "papers": cached.get("papers", []),
                "total_available": cached.get("total_available", 0),
                "cached": True,
                "query": query,
                "sort": sort
            }
    
    papers, total = fetch_pubmed_papers(query, max_results, sort)
    
    # Cache results
    papers_cache_col.update_one(
        {"query": cache_key},
        {"$set": {
            "papers": papers,
            "total_available": total,
            "cached_at": datetime.utcnow().isoformat(),
            "query": cache_key
        }},
        upsert=True
    )
    
    return {
        "papers": papers,
        "total_available": total,
        "cached": False,
        "query": query,
        "sort": sort
    }

# ─── NEWS (Latest PubMed + Trials) ──────────────────────────

@app.get("/api/news")
async def get_news(
    topic: str = "peptide research",
    limit: int = 15
):
    """Get latest peptide news (from recent PubMed papers and trial updates)"""
    cache_key = f"news_{topic}_{limit}"
    
    cached = news_cache_col.find_one({"query": cache_key})
    if cached:
        cached_time = datetime.fromisoformat(cached.get("cached_at", "2000-01-01"))
        if datetime.utcnow() - cached_time < timedelta(hours=2):
            return {
                "news": cached.get("news", []),
                "total": len(cached.get("news", [])),
                "cached": True,
                "topic": topic
            }
    
    news_items = []
    
    # Get recent papers as news
    papers, _ = fetch_pubmed_papers(topic, max_results=limit, sort="date")
    for paper in papers:
        news_items.append({
            "type": "paper",
            "title": paper["title"],
            "source": paper["journal"],
            "date": paper["pub_date"],
            "url": paper["url"],
            "authors": paper["authors"],
            "summary": f"Published in {paper['journal']}",
            "tags": ["research", "publication"]
        })
    
    # Get recent trial updates
    trials = fetch_clinical_trials(topic, page_size=limit)
    for trial in trials[:limit // 2]:
        news_items.append({
            "type": "trial",
            "title": trial["title"],
            "source": f"ClinicalTrials.gov ({trial['nct_id']})",
            "date": trial.get("last_updated", trial.get("start_date", "")),
            "url": trial["url"],
            "authors": [trial["sponsor"]],
            "summary": f"Status: {trial['status']} | Phase: {trial['phase']}",
            "tags": ["clinical trial", trial["status"].lower().replace("_", " ")]
        })
    
    # Sort by date (newest first)
    news_items.sort(key=lambda x: x.get("date", ""), reverse=True)
    news_items = news_items[:limit]
    
    # Cache
    news_cache_col.update_one(
        {"query": cache_key},
        {"$set": {"news": news_items, "cached_at": datetime.utcnow().isoformat(), "query": cache_key}},
        upsert=True
    )
    
    return {
        "news": news_items,
        "total": len(news_items),
        "cached": False,
        "topic": topic
    }

# ─── STATS ───────────────────────────────────────────────────

@app.get("/api/stats")
async def get_stats():
    """Get platform statistics"""
    peptide_count = peptides_col.count_documents({})
    
    return {
        "peptides_in_db": peptide_count,
        "total_peptides_tracked": len(IMPORTANT_PEPTIDES),
        "data_sources": ["ClinicalTrials.gov", "PubMed", "AI-Generated"],
        "last_updated": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
