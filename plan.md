# Development Plan — Premium Peptide Research Website (Bilingual)

## 1) Objectives (Updated Status)
- Deliver a **premium, light/clean, medical-grade** peptide research website with **DE/EN toggle**.
- Provide a **Peptide Encyclopedia** (MongoDB) combining **AI-generated structured profiles** + live links to **PubMed/ClinicalTrials.gov**.
- Provide **live study tracking** focused on **Eli Lilly + major pharma** using **ClinicalTrials.gov v2**.
- Provide **scientific paper tracking** using **PubMed E-utilities**.
- Provide a **news feed** for peptide-related developments.
- Use **high-end motion** (subtle gradients + hover micro-interactions + glass UI); keep animation tasteful and performance-safe.

**Current status:**
- ✅ Phase 1 POC complete (all integration tests passed)
- ✅ Phase 2 V1 MVP complete (backend + frontend + bilingual + data sources + premium UI)
- ⏳ Seeding in progress: **17/20** initial important peptides generated

---

## 2) Implementation Steps (Phased)

### Phase 1 — Core Workflow POC (Isolation) ✅ COMPLETED
**Core = “Fetch real studies + papers + generate/stash peptide profile reliably”**

**Completed outputs**
- Standalone POC script validating:
  - ✅ ClinicalTrials.gov v2 access (request method corrected; 403 fixed by switching to `requests` + headers)
  - ✅ PubMed search + summaries
  - ✅ OpenAI generation via **Emergent LLM key** with strict JSON
  - ✅ MongoDB upsert + retrieval
  - ✅ Combined pipeline

**Exit criteria (met)**
- ✅ One command produces a MongoDB document with generated bilingual peptide profile + retrievable source data.

---

### Phase 2 — V1 App Development (MVP, no auth) ✅ COMPLETED
**Architecture (as built)**
- Frontend: **React (CRA + Craco)** + Tailwind + shadcn/ui + Framer Motion
- Backend: **FastAPI**
- DB: **MongoDB**
- Integrations:
  - ✅ OpenAI (via Emergent proxy key)
  - ✅ ClinicalTrials.gov v2
  - ✅ PubMed E-utilities
  - ⚠️ News: implemented as an aggregated “news” stream combining **recent PubMed papers + recent ClinicalTrials.gov trial updates** (no external News API key yet)

**User stories (V1) — delivered**
1. ✅ Bilingual toggle DE/EN switching UI + peptide content
2. ✅ Encyclopedia search + premium peptide detail pages (indications/benefits/dosage/safety/research status)
3. ✅ Live studies page w/ filters (company chips incl. Eli Lilly, status)
4. ✅ Papers page w/ PubMed links + sorting
5. ✅ News page showing latest publications and trial updates

**Backend (FastAPI) — delivered endpoints**
- ✅ `GET /api/health`
- ✅ `GET /api/stats`
- ✅ `GET /api/peptides?query=&category=&page=&limit=`
- ✅ `GET /api/peptides/categories`
- ✅ `GET /api/peptides/{slug}`
- ✅ `POST /api/peptides/generate` (AI generate/refresh)
- ✅ `POST /api/peptides/seed` (background seeding)
- ✅ `GET /api/peptides/seed/status`
- ✅ `GET /api/trials?query=&company=&status=&page_size=`
- ✅ `GET /api/papers?query=&sort=&max_results=`
- ✅ `GET /api/news?topic=&limit=`

**Frontend — delivered pages**
- ✅ Home (hero search + live stats + featured peptides + latest trials + recent papers)
- ✅ Encyclopedia (search + category filter + generate profile on empty state)
- ✅ Peptide Detail (tabs: Overview, Mechanism, Dosage, Safety, Studies, Papers)
- ✅ Studies (search + status filter + company chips)
- ✅ Papers (search + relevance/date sorting)
- ✅ News (featured item + feed)

**Design — delivered**
- ✅ Premium light/clean aesthetic
- ✅ Glass navbar, clean typography (Space Grotesk + IBM Plex)
- ✅ Subtle hero gradient + noise overlay
- ✅ Hover micro-interactions (no `transition: all`)

**Testing (end of Phase 2)**
- ✅ Testing agent report: Backend **100%**, Frontend **95%**
- ✅ Manual verification via screenshots: home, studies, encyclopedia, peptide detail, bilingual switching

**Data status (V1)**
- ⏳ Seeding in progress: **17/20** important peptides generated (continues asynchronously)
- ✅ Real-time trials and papers fetched live with caching

---

### Phase 3 — Feature Expansion (quality + automation) 🔜 READY (Not Started)
**User stories (Expansion)**
1. Save an **Eli Lilly** filter and return instantly (saved searches)
2. Weekly digest page (“What’s new this week”), optional email later
3. Compare two peptides side-by-side (compare view)
4. Show “Last updated”, source counts, and freshness indicators per peptide
5. Feedback/report issue on peptide page

**Build steps (revised based on current MVP)**
- Automation & refresh
  - Add scheduled refresh (cron-ready job runner) for:
    - trials cache refresh (e.g., every 6–12h)
    - papers refresh (daily)
    - news aggregation refresh (daily)
  - Persist `last_updated` timestamps per peptide + per source
- Data model upgrades
  - Add `sources: { trials: [...], papers: [...], news: [...] }` to peptide docs (optional denormalization)
  - Company normalization (Eli Lilly variants) and trial status mapping
  - Add citations section and copy-to-clipboard citation actions
- UX upgrades
  - Saved filters/searches (localStorage first)
  - Compare page with key fields (mechanism, indications, safety, dosing, research status)
  - Advanced filters (phase, condition, sponsor)
- Observability
  - Add structured logs for upstream API failures, cache hit ratios
  - Light request timing metrics (middleware)

**Testing (end of Phase 3)**
- E2E: saved filters, compare flow, refresh pipeline, regression on Phase 2 pages

---

### Phase 4 — Production Hardening + Auth (only after approval) 🔜 FUTURE
**User stories (Hardening/Auth)**
1. Accounts to save peptides/searches across devices
2. Notification preferences
3. Admin approval/edit workflow + “verified” content
4. Manual refresh triggers + job status
5. Export peptide summary (PDF/markdown)

**Build steps**
- Auth (JWT) + roles (admin/editor/user)
- Admin panel + audit trail
- Security: rate limiting, API key handling, security headers
- Performance: pagination everywhere, caching strategy, image optimization

**Testing (end of Phase 4)**
- Full regression including auth + role permissions

---

## 3) Next Actions (Updated)
1. **Let seeding finish** (remaining 3 peptides). Optionally add a UI indicator + “seed now” admin-only button.
2. Decide whether to integrate an external **News API** (key required) or keep the current “papers+trials news” approach.
3. Start Phase 3 with the highest ROI items:
   - Saved Eli Lilly filter + advanced filtering
   - “Last updated” + source counts + freshness indicators
   - Scheduled refresh jobs

---

## 4) Success Criteria (Updated)
- ✅ POC: reliably generate and store a peptide document with real trials + papers + valid bilingual AI profile.
- ✅ V1: premium UI; bilingual toggle; encyclopedia + studies + papers + news all functional.
- ✅ Data integrity: stable links (NCT/PMID), caching in place.
- ✅ Design: light/clean aesthetic with tasteful motion; responsive; not “AI template” looking.
- Phase 3 target: automated refresh + saved filters + compare + improved data freshness visibility.
