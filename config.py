class Config:
    WC_WEIGHTS = {"batting": 0.4, "bowling": 0.4, "fielding": 0.2}

    STABILITY_THRESHOLDS = {
        "high": 80,
        "stable": 50,
        "volatile": 20
    }

    MAX_SCORE = 100
    MIN_SCORE = 0


config = Config()
