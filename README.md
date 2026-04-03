# PeptideDB - Peptide Research Intelligence Platform

A full-stack web application for exploring, comparing, and researching therapeutic peptides. Built with **React**, **FastAPI**, and **MongoDB**.

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-47A248?logo=mongodb&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-06B6D4?logo=tailwindcss&logoColor=white)

---

## Features

- **Peptide Encyclopedia** - 48 scientifically accurate peptide profiles with bilingual content (DE/EN)
- **Peptide Comparison** - Side-by-side comparison of multiple peptides
- **Clinical Trials Integration** - Live data from ClinicalTrials.gov v2 API
- **PubMed Papers** - Real-time research paper search via PubMed E-utilities
- **Full-Text Search** - Search across all peptide names, categories, and descriptions
- **Category Filtering** - Browse peptides by 31+ therapeutic categories
- **Dark Mode** - Fully themed dark/light mode with smooth transitions
- **Bilingual (DE/EN)** - Complete German and English translations via react-i18next
- **Glossary** - Searchable glossary of peptide-related scientific terms

## Tech Stack

### Frontend
- **React 19** with React Router v7
- **Tailwind CSS** + **shadcn/ui** component library
- **Framer Motion** for animations
- **react-i18next** for internationalization
- **Recharts** for data visualization
- **Axios** for API communication

### Backend
- **FastAPI** (Python 3.12+)
- **MongoDB** with PyMongo
- **ClinicalTrials.gov v2 API** integration
- **PubMed E-utilities** integration
- CORS-enabled REST API

### Database
- **MongoDB 7** (Docker)
- Text indexes for full-text search
- 48 pre-built peptide profiles across 31 categories

## Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker (for MongoDB)

### 1. Start MongoDB
```bash
docker run -d --name peptidedb-mongo -p 27017:27017 -v peptidedb-data:/data/db mongo:7
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python seed_data.py           # Insert 20 base peptides
python seed_data_extended.py  # Insert 28 additional peptides
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm start
```

The app will be available at **http://localhost:3000**.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/peptides` | List all peptides (with search, filter, pagination) |
| GET | `/api/peptides/{slug}` | Get peptide detail by slug |
| GET | `/api/peptides/compare` | Compare multiple peptides side-by-side |
| GET | `/api/peptides/categories` | List all categories |
| GET | `/api/trials` | Search ClinicalTrials.gov |
| GET | `/api/papers` | Search PubMed papers |
| GET | `/api/stats` | Platform statistics |

## Peptide Categories

The database covers peptides across therapeutic areas including:

- GLP-1 / Metabolic (Semaglutide, Tirzepatide, Retatrutide, ...)
- Growth Hormone Secretagogues (Ipamorelin, CJC-1295, GHRP-6, ...)
- Healing & Recovery (BPC-157, TB-500, Thymosin Beta-4, ...)
- Neuropeptides (Selank, Semax, Dihexa, ...)
- Anti-Aging & Longevity (Epitalon, GHK-Cu, FOXO4-DRI, Humanin, ...)
- Antimicrobial (LL-37, Defensin Alpha-1, ...)
- Immune & Inflammation (Thymosin Alpha 1, Thymalin, VIP, ...)
- Cosmetic & Skin (Matrixyl, AHK-Cu, ...)
- And more...

## Project Structure

```
PeptideDB/
├── backend/
│   ├── server.py                 # FastAPI application
│   ├── seed_data.py              # 20 base peptide profiles
│   └── seed_data_extended.py     # 28 additional peptide profiles
├── frontend/
│   ├── src/
│   │   ├── components/ui/        # shadcn/ui components
│   │   ├── pages/
│   │   │   ├── HomePage.js       # Dashboard with live stats
│   │   │   ├── EncyclopediaPage.js  # Peptide listing & search
│   │   │   ├── PeptideDetailPage.js # Detailed peptide view
│   │   │   ├── ComparePage.js    # Peptide comparison
│   │   │   ├── StudiesPage.js    # Clinical trials browser
│   │   │   └── GlossaryPage.js   # Scientific glossary
│   │   ├── i18n/                 # DE/EN translations
│   │   └── lib/api.js            # API client
│   └── package.json
└── README.md
```

## Screenshots

*Dark mode peptide encyclopedia with search and category filtering*

## License

This project is for demonstration and educational purposes.
