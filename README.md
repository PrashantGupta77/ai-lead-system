# AI Lead Qualification System

Production-ready AI-powered Lead Qualification and Smart Response Platform built using FastAPI, Groq LLM, Streamlit, MySQL, Docker, and Render.

The system automatically classifies incoming leads into HOT, WARM, and COLD categories, generates contextual AI responses, tracks lead analytics, and provides an admin dashboard for monitoring lead activity.

---

# Live Demo

## Frontend (Streamlit UI)

https://ai-lead-system-ui.onrender.com

## Backend API

https://ai-lead-system-jkto.onrender.com

## Swagger Documentation

https://ai-lead-system-jkto.onrender.com/docs

---

# Features

### AI Lead Qualification

* HOT / WARM / COLD lead classification
* Hybrid Rule Engine + LLM fallback
* Confidence scoring
* Business intent detection
* Curiosity signal detection
* Urgency detection

### AI Response Generation

* Context-aware responses
* Lead-type specific responses
* Retry mechanism
* Fallback response handling

### Authentication & Security

* JWT Authentication
* Password hashing using bcrypt
* Role-Based Access Control (RBAC)
* Admin/User authorization

### Admin Dashboard

* Lead analytics
* HOT/WARM/COLD distribution
* Recent lead monitoring
* User management
* Audit logging

### Production Features

* Dockerized deployment
* Railway MySQL database
* Render deployment
* Automated testing
* CI/CD ready architecture
* Health monitoring

---

# Tech Stack

| Layer             | Technology                  |
| ----------------- | --------------------------- |
| Frontend          | Streamlit                   |
| Backend           | FastAPI                     |
| AI Model          | Groq (Llama 3.1 8B Instant) |
| Database          | MySQL                       |
| ORM               | SQLAlchemy                  |
| Authentication    | JWT                         |
| Password Security | bcrypt                      |
| Testing           | Pytest                      |
| Containerization  | Docker                      |
| Deployment        | Render                      |
| Database Hosting  | Railway                     |
| CI/CD             | GitHub Actions              |

---

# System Architecture

```text
                    ┌──────────────────┐
                    │   Streamlit UI   │
                    │    Frontend      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  FastAPI Backend │
                    └────────┬─────────┘
                             │
           ┌─────────────────┼─────────────────┐
           ▼                                   ▼

   Rule-Based Engine                     Groq LLM
   Intent Scoring                        Classification
   Signal Detection                      Response Generation

           └─────────────────┬─────────────────┘
                             ▼

                  Lead Classification Engine

                             ▼

                     MySQL Database
                        (Railway)

                             ▼

                    Admin Dashboard
                    Analytics & Logs
```

---

# Project Structure

```text
ai-lead-system/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── client.py
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── login.py
│   │   ├── lead_processing.py
│   │   └── admin_dashboard.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── auth.py
│
├── src/
│   │
│   ├── auth/
│   │   ├── dependencies.py
│   │   ├── fake_users.py
│   │   ├── passwords.py
│   │   ├── rbac.py
│   │   └── security.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── dependencies.py
│   │   ├── init_db.py
│   │   ├── init_admin.py
│   │   ├── repository.py
│   │   ├── user_repository.py
│   │   ├── lead_model.py
│   │   ├── user_model.py
│   │   ├── audit_log_model.py
│   │   └── audit_repository.py
│   │
│   ├── evaluation/
│   │   ├── evaluator.py
│   │   └── metrics.py
│   │
│   ├── exceptions/
│   │   └── handlers.py
│   │
│   ├── monitoring/
│   │   └── performance.py
│   │
│   ├── services/
│   │   └── lead_service.py
│   │
│   ├── llm.py
│   ├── pipeline.py
│   ├── scoring.py
│   ├── validators.py
│   ├── prompts.py
│   ├── models.py
│   └── main.py
│
├── tests/
│   ├── test_api.py
│   ├── test_pipeline.py
│   ├── test_scoring.py
│   ├── test_validators.py
│   ├── test_llm_mocking.py
│   ├── test_evaluator.py
│   ├── test_metrics.py
│   ├── test_passwords.py
│   ├── test_security.py
│   └── test_monitoring.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# Lead Classification Logic

## HOT

* Requests pricing
* Requests demo
* Requests consultation
* Urgent implementation need
* Strong business intent

## WARM

* Evaluating solutions
* Interested in AI automation
* Looking for more information
* Moderate purchase intent

## COLD

* Browsing
* Researching
* General curiosity
* No buying signals

---

# API Endpoints

## Authentication

```text
POST /register
POST /login
GET  /me
```

## Lead Processing

```text
POST /process
```

## Admin

```text
GET /analytics
GET /recent-leads
GET /users
GET /audit-logs
PUT /users/{id}/role
```

---

# Testing

Run all tests:

```bash
pytest -v
```

Run coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

Current Status:

```text
24 Tests Passed
79% Test Coverage
```

---

# Docker Deployment

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Stop:

```bash
docker compose down
```

---

# Environment Variables

```env
GROQ_API_KEY=

MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_PORT=
MYSQL_DB=

SECRET_KEY=

ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
```

---

# Default Admin

The system automatically creates an admin account during first startup.

```text
Username: admin
Password: admin123
```

Change these credentials immediately in production.

---

# Future Improvements

* Alembic Database Migrations
* Prometheus Monitoring
* Grafana Dashboards
* Redis Queue
* Celery Background Jobs
* CRM Integrations
* ML-Based Lead Scoring
* Semantic Embeddings Search
* Lead Conversion Tracking

---

# Project Highlights

* Production-ready architecture
* End-to-end AI workflow
* Dockerized deployment
* Railway MySQL integration
* Render cloud deployment
* JWT Authentication
* Role-Based Access Control
* Streamlit Admin Dashboard
* Automated Testing
* CI/CD Ready

---

# Author

Prashant Kumar Gupta

MCA — University of Hyderabad

AI/ML Engineer | Generative AI | FastAPI | Machine Learning | LLM Applications
