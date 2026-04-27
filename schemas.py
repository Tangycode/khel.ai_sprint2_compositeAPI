from pydantic import BaseModel
from typing import List


class Player(BaseModel):
    player_id: str
    player_name: str


class MatchContext(BaseModel):
    match_id: str
    innings_id: str


class WCInput(BaseModel):
    match: MatchContext
    player: Player
    batting_scores: List[float]
    bowling_scores: List[float]
    fielding_scores: List[float]


class CAInput(BaseModel):
    match: MatchContext
    x_metric: List[float]
    y_metric: List[float]
    x_metric_name: str
    y_metric_name: str


class PVInput(BaseModel):
    match: MatchContext
    batting_scores: List[float]
    bowling_scores: List[float]
    fielding_scores: List[float]
