from fastapi import APIRouter
from app.schemas import WCInput, CAInput, PVInput
from app.services import weighted_contribution, correlation_analysis, performance_variance
from app.exceptions import KhelAIError
from app.logger import logger

router = APIRouter()


@router.post("/weighted-contribution")
def wc(data: WCInput):

    if not data.batting_scores:
        raise KhelAIError("EMPTY", "No batting data")

    return {
        "player": data.player,
        "match": data.match,
        "result": weighted_contribution(
            data.batting_scores,
            data.bowling_scores,
            data.fielding_scores
        )
    }


@router.post("/correlation-analysis")
def ca(data: CAInput):

    if len(data.x_metric) != len(data.y_metric):
        raise KhelAIError("MISMATCH", "Length mismatch")

    return {
        "x": data.x_metric_name,
        "y": data.y_metric_name,
        "result": correlation_analysis(data.x_metric, data.y_metric)
    }


@router.post("/performance-variance")
def pv(data: PVInput):

    return {
        "match": data.match,
        "result": performance_variance(
            data.batting_scores,
            data.bowling_scores,
            data.fielding_scores
        )
    }
