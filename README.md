# Khel AI Sprint 2 — Cricket Intelligence Backend

## Overview

Khel AI Sprint 2 is a FastAPI-based cricket analytics backend that converts raw match data into structured, explainable intelligence.

It is designed for:
- dashboards
- AI agents
- performance analysis systems
- cricket decision engines

---

## Core Modules

This system exposes 3 independent analytics engines:

### 1. Weighted Contribution (WC)
Calculates player impact using weighted cricket metrics.

### 2. Correlation Analysis (CA)
Measures relationship between two performance metrics using Pearson correlation.

### 3. Performance Variance (PV)
Measures consistency and stability of player performance over time.

---

# Architecture


main.py
↓
api/player_intelligence.py
↓
services.py
↓
schemas.py
↓
config.py
↓
exceptions.py
↓
logger.py


---

# Base URL


/api/v1/player-intelligence/


---

# Endpoints

---

## Weighted Contribution (WC)

### Endpoint

POST /weighted-contribution


### Purpose
Computes overall player impact score.

### Input
Requires:
- match context
- player info
- batting_scores
- bowling_scores
- fielding_scores

### Output
- batting_score
- bowling_score
- fielding_score
- total_score
- derived metrics:
  - strike_efficiency
  - run_impact
  - economy_impact
  - fielding_impact

### Formula

total_score =
0.4 * batting +
0.4 * bowling +
0.2 * fielding


---

# Correlation Analysis (CA)

### Endpoint

POST /correlation-analysis


### Purpose
Measures statistical relationship between two cricket metrics.

### Output
- correlation_value (Pearson)
- direction (positive / negative)
- strength (weak / moderate / strong)
- interpretation
- sample_size
- pairs_used
- formula_name

### Validation Rules
- arrays must match length
- minimum 2 values required
- zero variance not allowed

---

#Performance Variance (PV)

### Endpoint

POST /performance-variance


### Purpose
Measures consistency vs volatility in performance.

### Output
- batting_variance
- bowling_variance
- fielding_variance
- overall_variance
- stability_index (0–100)
- interpretation

### Stability Scale

| Score | Label |
|------|------|
| > 80 | Highly Stable |
| 50–80 | Stable |
| 20–50 | Volatile |
| < 20 | Highly Volatile |

### Special Case
If variance = 0:

stability_index = 100
note = "perfectly stable sample"


---

# Validation Rules

All endpoints enforce strict validation:

- empty arrays → 400 error
- mismatched metric lengths → 400 error
- missing match_id / innings_id → 400 error
- insufficient data (<2 points) → 400 error
- invalid numeric values → rejected

---
# System Features

- FastAPI backend
- CORS enabled
- /health endpoint (Render uptime check)
- / root endpoint (status check)
- config-driven weights
- centralized error handling
- service-layer architecture

---

# Test Payloads

Located in:


/test_payloads/


Includes:

### normal.json
Standard match scenario

### empty.json
Empty dataset (validation test)

### edge.json
Zero variance / extreme stability case

---

# Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
 Health Check
GET /health
