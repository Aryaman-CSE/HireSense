# HireSense

> AI-powered Recruitment Intelligence Platform built with FastAPI, Groq LLMs, and SQLAlchemy.

HireSense analyzes resumes and job descriptions using Large Language Models, stores structured intelligence, and performs explainable semantic matching between candidates and job requirements.

Unlike traditional keyword-based ATS systems, HireSense extracts structured information from resumes and job descriptions before performing transparent, skill-based matching.

---

## Features

- AI-powered Resume Intelligence
- AI-powered Job Description Intelligence
- Explainable Semantic Matching Engine
- ATS Readiness Analysis
- Persistent Resume Repository
- Persistent Job Repository
- REST API built with FastAPI
- Interactive Swagger API Documentation
- Modular Backend Architecture

---

## Architecture

```
                Resume Upload
                      │
                      ▼
           AI Resume Intelligence
                      │
                      ▼
              Resume Repository
                      │
                      │
Job Upload ───────► AI Job Intelligence
                      │
                      ▼
               Job Repository
                      │
                      ▼
          Semantic Match Engine
                      │
                      ▼
          Explainable Match Report
```

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Backend | FastAPI |
| AI | Groq API (Llama 3.3 70B) |
| Database | SQLite |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Document Parsing | PyMuPDF, python-docx |
| API Docs | Swagger / OpenAPI |

---

## Project Structure

```
backend/
│
├── app/
│   ├── ai/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── matching/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   └── services/
│
├── tests/
│
└── uploads/
```

---

## API Endpoints

### Resume APIs

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/resumes/upload` |
| GET | `/api/v1/resumes` |
| GET | `/api/v1/resumes/{id}` |
| DELETE | `/api/v1/resumes/{id}` |

### Job APIs

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/jobs/upload` |
| GET | `/api/v1/jobs` |
| GET | `/api/v1/jobs/{id}` |
| DELETE | `/api/v1/jobs/{id}` |

### Matching

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/matches` |

---

## Running Locally

Clone the repository

```bash
git clone https://github.com/Aryaman-CSE/HireSense.git
cd HireSense
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

Run the server

```bash
python -m uvicorn backend.app.main:app --reload --reload-dir backend
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

## Current Status

### Completed

- Resume Intelligence
- Job Intelligence
- Resume Repository
- Job Repository
- Semantic Match Engine
- Explainable Matching API
- Persistent Database Layer

### In Progress

- Recruiter Dashboard
- Candidate Ranking
- Advanced Search
- Frontend Application

---

## Author

**Aryaman Singh**

Computer Science Engineering (AI & ML)

GitHub: https://github.com/Aryaman-CSE