# khel.ai_sprint2_compositeAPI
# Khel AI Sprint 2

## Overview
Cricket intelligence backend with 3 core analytics APIs:
- Weighted Contribution (WC)
- Correlation Analysis (CA)
- Performance Variance (PV)

---

## Architecture
- FastAPI backend
- Service-layer computation
- Schema validation layer
- Router-only main.py

---

## Endpoints

### WC
POST /api/v1/player-intelligence/weighted-contribution

### CA
POST /api/v1/player-intelligence/correlation-analysis

### PV
POST /api/v1/player-intelligence/performance-variance

---

## Rules
- Model-shaped inputs only (match, innings, players, ball_events)
- Strict validation for empty/mismatched arrays
- No calculations in main.py

---

## Run locally
```bash
uvicorn app.main:app --reload

Health Check

GET /health

Author

Khel AI System
