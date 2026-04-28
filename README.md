#  khel.ai_sprint2_compositeAPI

##  Overview

Khel AI Sprint 2 is a production-grade FastAPI backend that converts raw cricket match data into explainable intelligence outputs.

It is designed for:
- analytics dashboards
- AI agents
- performance evaluation systems
- real-time cricket intelligence engines

---

#  System Architecture


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

#  Base Route


/api/v1/player-intelligence/


---

#  Endpoints

---

##  Weighted Contribution (WC)

### Endpoint

POST /weighted-contribution


### Purpose
Computes overall player performance impact using weighted cricket metrics.

---

### Input Schema
```json id="wc_in_100"
{
  "match": {
    "match_id": "M1",
    "innings_id": "I1"
  },
  "player": {
    "player_id": "P1",
    "player_name": "Virat Test"
  },
  "batting_scores": [45, 60, 30],
  "bowling_scores": [2, 1, 3],
  "fielding_scores": [1, 2, 1]
}
``` id="wc_in_100"

---

### Output Schema
```json id="wc_out_100"
{
  "player": {
    "player_id": "P1",
    "player_name": "Virat Test"
  },
  "match": {
    "match_id": "M1",
    "innings_id": "I1"
  },
  "result": {
    "batting_score": 45.0,
    "bowling_score": 2.0,
    "fielding_score": 1.3,
    "total_score": 19.92,
    "derived_metrics": {
      "strike_efficiency": 49.5,
      "run_impact": 40.5,
      "economy_impact": 2.1,
      "fielding_impact": 1.3
    },
    "formula": "0.4*batting + 0.4*bowling + 0.2*fielding"
  }
}
``` id="wc_out_100"

---

### Validation Errors
- EMPTY_INNINGS
- INVALID_SCORE_ARRAY
- MISSING_PLAYER_DATA

---

##  Correlation Analysis (CA)

### Endpoint

POST /correlation-analysis


---

### Input Schema
```json id="ca_in_100"
{
  "match": {
    "match_id": "M1",
    "innings_id": "I1"
  },
  "x_metric_name": "batting",
  "y_metric_name": "bowling",
  "x_metric": [10, 20, 30],
  "y_metric": [1, 2, 3]
}
``` id="ca_in_100"

---

### Output Schema
```json id="ca_out_100"
{
  "x_metric_name": "batting",
  "y_metric_name": "bowling",
  "sample_size": 3,
  "result": {
    "formula_name": "Pearson correlation",
    "correlation_value": 0.98,
    "direction": "positive",
    "strength": "strong",
    "interpretation": "strong positive relationship"
  }
}
``` id="ca_out_100"

---

### Validation Errors
- MISMATCH_LENGTH
- INSUFFICIENT_DATA
- ZERO_VARIANCE

---

##  Performance Variance (PV)

### Endpoint

POST /performance-variance


---

### Input Schema
```json id="pv_in_100"
{
  "match": {
    "match_id": "M1",
    "innings_id": "I1"
  },
  "batting_scores": [50, 50, 50],
  "bowling_scores": [0, 0, 0],
  "fielding_scores": [10, 10, 10]
}
``` id="pv_in_100"

---

### Output Schema
```json id="pv_out_100"
{
  "match": {
    "match_id": "M1",
    "innings_id": "I1"
  },
  "result": {
    "batting_variance": 0.0,
    "bowling_variance": 0.0,
    "fielding_variance": 0.0,
    "overall_variance": 0.0,
    "stability_index": 100,
    "interpretation": "Highly Stable",
    "note": "perfectly stable sample"
  }
}
``` id="pv_out_100"

---

#  Global Validation Rules

All endpoints enforce:

- empty arrays → 400 error
- mismatched lengths → 400 error
- missing match_id → 400 error
- missing innings_id → 400 error
- non-numeric values → rejected
- insufficient data (<2 points) → 400 error

---

#  System Features

- FastAPI backend
- CORS enabled
- /health endpoint (Render uptime check)
- / root endpoint (status)
- config-driven weights
- centralized error handling
- service-layer architecture

---

#  Versioning Strategy

Current version:

/api/v1/


Upgrade policy:
- v1 endpoints remain backward compatible
- v2 will extend outputs, NOT break v1 contracts

---

#  Test Payloads

Located in:

/test_payloads/


Includes:
- normal case
- empty dataset
- edge case (zero variance)

---

#  Run Instructions
pip install -r requirements.txt
uvicorn app.main:app --reload
Health Check
GET /health
