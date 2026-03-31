# Development Plan — Premium Peptide Research Website (Bilingual)

## 1) Objectives
- Deliver a **premium, light/clean, medical-grade** peptide research website with **DE/EN toggle**.
- Build a **Peptide Encyclopedia** (MongoDB) combining **AI-generated structured profiles** + citations/links to **PubMed/ClinicalTrials.gov**.
- Provide **live study tracking** focused on **Eli Lilly + major pharma** using **ClinicalTrials.gov** and paper discovery via **PubMed**.
- Provide a **scientific/economic news feed** about peptides (News API) with tagging and search.
- Use **high-end motion** (subtle gradients + particles + molecule/DNA motifs) without hurting readability/performance.

## 2) Implementation Steps (Phased)

### Phase 1 — Core Workflow POC (Isolation) (must pass before app build)
**Core = “Fetch real studies + papers + generate/stash peptide profile reliably”**

**User stories (POC)**
1. As a user, I want to search a peptide name and get a structured profile draft in seconds.
2. As a user, I want to see real **ClinicalTrials.gov** trials for a query (e.g., “tirzepatide”, “Eli Lilly”).
3. As a user, I want to see real **PubMed** papers for the same query with titles/authors/links.
4. As a user, I want the system to merge results into one normalized object (peptide + trials + papers).
5. As a developer, I want the object saved in MongoDB and retrievable by slug/id.

**POC tasks**
- Web research (quick): confirm best-practice endpoints + rate limits for:
  - ClinicalTrials.gov v2 API (studies search, sponsor filter)
  - NCBI E-utilities (esearch + esummary/efetch)
  - Pick a News API provider and validate query capabilities
- Write **standalone Python scripts** (no app) to prove:
  - ClinicalTrials.gov query by keyword + sponsor/company returns trials
  - PubMed query returns papers
  - OpenAI call generates **strict JSON** peptide profile (DE+EN fields)
  - MongoDB insert/read works for the resulting document
- Define the canonical schema (minimal but extensible):
  - `peptide`: names, synonyms, mechanism, indications, benefits, risks, dosing (research-only disclaimer), regulatory/research status
  - `sources`: trials[], papers[], news[] with stable URLs/ids
  - `i18n`: `de`, `en` blocks (or per-field translations)
- “Fix until works”: retries/backoff, JSON validation, dedupe logic (trial id, PMID), basic caching.

**Exit criteria (POC)**
- One command produces a MongoDB document for a peptide query containing:
  - ≥5 trials (when available), ≥5 papers (when available), AI profile JSON valid
  - Deterministic parsing + no manual edits

---

### Phase 2 — V1 App Development (MVP, no auth)
**Architecture**
- Frontend: React (Vite/Next) + Tailwind (or equivalent) + Framer Motion
- Background motion: lightweight particles + subtle animated gradients; optional Three.js molecule scene behind hero
- Backend: FastAPI
- DB: MongoDB
- Integrations: OpenAI (Emergent key), ClinicalTrials.gov, PubMed, News API

**User stories (V1)**
1. As a user, I can toggle **Deutsch/English** and the UI + peptide content switches accordingly.
2. As a user, I can search peptides and open a **clean detail page** with indications/benefits/risks/dosing/research status.
3. As a user, I can view **Live Studies** and filter by company (Eli Lilly) and status (recruiting/completed).
4. As a user, I can view **Papers** with PubMed links and sort by relevance/date.
5. As a user, I can read a **News feed** about peptides and open the source article.

**Build steps**
- Backend (FastAPI)
  - Endpoints:
    - `GET /api/peptides?query=` (search)
    - `GET /api/peptides/{slug}` (details)
    - `POST /api/peptides/generate` (LLM generate/refresh; admin-like but unauthenticated for MVP)
    - `GET /api/trials?query=&company=&status=` (ClinicalTrials.gov)
    - `GET /api/papers?query=` (PubMed)
    - `GET /api/news?query=&topic=` (News API)
  - Normalization + dedupe + caching layer (Mongo collection for cached API responses)
  - Background jobs (simple polling endpoint/cron-ready structure; actual cron later)
  - Strong validation (Pydantic models) and citation fields
- Frontend
  - Pages: Home (hero + search), Encyclopedia (list), Peptide detail, Studies, Papers, News
  - Premium UI kit: typography scale, spacing system, cards, tables, skeleton loaders, empty states
  - Motion: scroll-based reveals; subtle background gradient animation; particles in hero; ensure accessibility/reduced-motion
  - i18n: JSON dictionaries + content selection from API response
- Seed initial “important peptides” list (curated starter set) and generate profiles on demand.

**Testing (end of Phase 2)**
- One end-to-end pass:
  - Search peptide → detail page renders
  - Trials/papers/news fetch correctly
  - Language toggle works across pages
  - No layout breaks on mobile/desktop

---

### Phase 3 — Feature Expansion (quality + automation)
**User stories (Expansion)**
1. As a user, I can track **Eli Lilly** as a saved filter and return to it instantly.
2. As a user, I can subscribe to “What’s new this week” (digest page; email later).
3. As a user, I can compare two peptides side-by-side.
4. As a user, I can see “Last updated” timestamps and source counts per peptide.
5. As a user, I can report an issue on a peptide page (feedback form).

**Build steps**
- Scheduled refresh (cron-ready):
  - Update trials/papers/news snapshots daily
  - Refresh AI profiles when sources change materially
- Data quality upgrades:
  - Company normalization (Eli Lilly synonyms), trial status mapping, tagging
  - Source citations section on each peptide page
- UX upgrades:
  - Advanced filters (company, phase, condition)
  - Compare view, saved searches (local storage in MVP)
- Observability:
  - Basic logging, request timing, API error dashboards (lightweight)

**Testing (end of Phase 3)**
- E2E: saved filters, compare, refresh pipeline, regression on V1 flows.

---

### Phase 4 — Production Hardening + Auth (only after approval)
**User stories (Hardening/Auth)**
1. As a user, I can create an account to save peptides and searches across devices.
2. As a user, I can manage notification preferences.
3. As an admin, I can approve/edit peptide profiles and lock “verified” content.
4. As an admin, I can trigger manual refresh and see job status.
5. As a user, I can export a peptide summary (PDF/markdown).

**Build steps**
- Add auth (JWT) + roles (admin/editor/user)
- Admin panel for curation + audit trail
- Rate limiting, API key handling, security headers
- Performance: CDN-friendly assets, image optimization, pagination everywhere

**Testing (end of Phase 4)**
- Full regression including auth + role permissions.

## 3) Next Actions
1. Lock initial schema (peptide profile JSON + sources + bilingual structure).
2. Select News API provider and confirm query limits.
3. Implement Phase 1 POC scripts (ClinicalTrials.gov + PubMed + OpenAI + Mongo) and iterate until stable.
4. Once POC passes, scaffold FastAPI + React and implement Phase 2 MVP screens/endpoints.

## 4) Success Criteria
- POC: can reliably generate and store a peptide document with real trials + papers + valid bilingual AI profile.
- V1: fast, premium UI; bilingual toggle; encyclopedia + studies + papers + news all functional.
- Data integrity: deduped sources, stable links (NCT/PMID), visible “last updated”.
- Design: light/clean aesthetic, tasteful motion, accessible, responsive; no “AI template” look.
