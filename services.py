import math
from config import config


def avg(arr):
    return sum(arr) / len(arr)


def weighted_contribution(batting, bowling, fielding):

    bat = avg(batting)
    bowl = avg(bowling)
    field = avg(fielding)

    w = config.WC_WEIGHTS

    total = (
        w["batting"] * bat +
        w["bowling"] * bowl +
        w["fielding"] * field
    )

    return {
        "batting_score": bat,
        "bowling_score": bowl,
        "fielding_score": field,
        "total_score": max(config.MIN_SCORE, min(config.MAX_SCORE, total)),
        "derived_metrics": {
            "strike_efficiency": bat * 1.1,
            "run_impact": bat * 0.9,
            "economy_impact": bowl * 1.05,
            "fielding_impact": field
        },
        "formula": "0.4 bat + 0.4 bowl + 0.2 field"
    }


def pearson(x, y):
    n = len(x)
    mx = sum(x)/n
    my = sum(y)/n

    num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    dx = sum((x[i]-mx)**2 for i in range(n))
    dy = sum((y[i]-my)**2 for i in range(n))

    if dx == 0 or dy == 0:
        return None

    return num / math.sqrt(dx * dy)


def correlation_analysis(x, y):
    r = pearson(x, y)

    if r is None:
        return {"error": "invalid_variance"}

    return {
        "formula": "Pearson",
        "correlation_value": r,
        "direction": "positive" if r > 0 else "negative",
        "strength": (
            "strong" if abs(r) > 0.7 else
            "moderate" if abs(r) > 0.4 else
            "weak"
        )
    }


def variance(arr):
    m = avg(arr)
    return sum((x-m)**2 for x in arr)/len(arr)


def performance_variance(bat, bowl, field):

    vb = variance(bat)
    vbo = variance(bowl)
    vf = variance(field)

    overall = (vb + vbo + vf) / 3

    if overall == 0:
        return {
            "stability_index": 100,
            "interpretation": "Highly Stable"
        }

    stability = min(100, (1 / (overall + 1e-6)) * 10)

    return {
        "batting_variance": vb,
        "bowling_variance": vbo,
        "fielding_variance": vf,
        "overall_variance": overall,
        "stability_index": stability
    }
