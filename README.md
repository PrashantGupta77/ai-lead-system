# AI Lead Qualification System

Production-oriented AI Lead Qualification + Smart Response System built using FastAPI, Groq LLM, and hybrid lead scoring logic.

This system:
- accepts lead input from forms/chat
- classifies leads into HOT / WARM / COLD
- generates contextual AI responses
- handles failures gracefully
- is designed with production scalability in mind

---

# Features

- Hybrid lead classification (rules + LLM fallback)
- AI-powered contextual response generation
- Confidence scoring
- Label-aware fallback responses
- FastAPI REST API
- Swagger API documentation
- Modular architecture
- Production-oriented design

---

# Tech Stack

| Layer | Technology |
|---|---|
| API | FastAPI |
| AI Model | Groq (Llama3-8B) |
| Validation | Pydantic |
| Environment | python-dotenv |
| Runtime | Uvicorn |
| Language | Python |

---

# Project Structure

```text
ai-lead-system/
│
├── .gitignore
├── requirements.txt
├── .env.example
├── README.md
│
└── src/
    ├── models.py
    ├── prompts.py
    ├── scoring.py
    ├── llm.py
    ├── pipeline.py
    ├── validators.py
    ├── main.py
│
├── samples/
    ├── cold_input.json
    ├── cold_output.json
    ├── hot_input.json
    ├── hot_output.json
    ├── low_quality_input.json
    ├── low_quality_output.json
    ├── warm_input.json
    ├── warm_output.json
```

---

# Architecture Flow

```text
Lead Input (Form / Chat)
            │
            ▼
      FastAPI Endpoint
            │
            ▼
     Validation Layer
            │
            ▼
    Rule-Based Scoring
            │
            ├── High confidence
            │       ▼
            │   Direct Classification
            │
            └── Low confidence
                    ▼
             LLM Classification
                    │
                    ▼
          Confidence Calculation
                    │
                    ▼
          AI Response Generation
                    │
                    ▼
             JSON API Response
```

---

# Lead Classification Logic

## HOT
- urgent buying intent
- scaling/business pressure
- immediate implementation signals

## WARM
- evaluating solutions
- interested but not urgent
- exploratory business intent

## COLD
- curiosity only
- informational questions
- no clear buying signal

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/PrashantGupta77/ai-lead-system.git
```

---

## 2. Navigate into Project

```bash
cd ai-lead-system
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run the Application

```bash
uvicorn src.main:app --reload
```

---

# API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

### GET `/`

Response:

```json
{
  "status": "running"
}
```

---

## Process Lead

### POST `/process`

### Request

```json
{
  "message": "We need AI automation urgently for our sales pipeline."
}
```

---

### Response

```json
{
  "label": "HOT",
  "confidence": 0.92,
  "response": "Thanks for reaching out — this looks urgent. Can we schedule a quick call today to help you get started immediately?"
}
```

---

# Example Test Cases

## HOT Lead

```json
{
  "message": "We need automation for our sales funnel urgently. We are scaling fast."
}
```

---

## WARM Lead

```json
{
  "message": "We are exploring AI tools for lead qualification."
}
```

---

## COLD Lead

```json
{
  "message": "I just saw your page. What do you do exactly?"
}
```

---

# Confidence Scoring

The system uses:
- rule-based intent scoring
- sigmoid normalization
- label-aware calibration

This produces stable probability-like confidence scores instead of arbitrary linear scaling.

---

# Fallback Handling

The system gracefully handles:

- LLM failures
- empty responses
- weak outputs
- ambiguous inputs
- low-quality leads

Fallback responses are label-aware to preserve conversational quality.

---

# Production-Oriented Design Choices

## Why Hybrid Classification?

Rules:
- fast
- cheap
- deterministic

LLM:
- flexible
- contextual
- semantic understanding

Using both improves:
- latency
- reliability
- cost efficiency

---

# Challenges Faced

## 1. Overclassification of Curiosity Leads

Early versions incorrectly classified informational queries as WARM.

### Solution

Added TOFU (Top-of-Funnel) curiosity detection signals.

---

## 2. Generic Fallback Responses

Initial fallback responses ignored lead intent.

### Solution

Implemented label-aware fallback responses.

---

## 3. Confidence Calibration

Linear confidence scaling produced unstable scores.

### Solution

Replaced heuristic scaling with sigmoid-based normalization.

---

# Future Improvements

## 1. Replace Rules with ML Classifier

Use:
- Logistic Regression
- XGBoost
- Transformer-based classifiers

---

## 2. Add Embeddings

Semantic lead understanding using:
- sentence-transformers
- vector similarity

---

## 3. Add Async Queue

Use:
- Redis
- Celery

For:
- retries
- scalability
- non-blocking processing

---

## 4. CRM Integration

Push HOT leads to:
- HubSpot
- Salesforce
- Zoho

---

## 5. Monitoring & Observability

Add:
- Prometheus
- Grafana
- Sentry

Track:
- latency
- LLM failures
- lead distribution
- conversion metrics

---

# Design Trade-Offs

| Decision | Trade-Off |
|---|---|
| Rule + LLM Hybrid | Simpler than full ML pipeline |
| FastAPI | Lightweight but minimal enterprise tooling |
| Prompt Engineering | Faster MVP than model fine-tuning |
| Rule-Based Signals | Easy debugging but less semantic |

---

# Why This Approach?

The focus of this project was:
- clarity over complexity
- production awareness
- reliability
- modularity
- scalability

Instead of overengineering the system, the implementation prioritizes maintainability and real-world deployment practicality.

---

# Loom Video:
```text
https://www.loom.com/share/22ed77e2905b4c9f8ec369ea8999eb22
```
---

# Author

Prashant Gupta
