from cgitb import reset
from dataclasses import dataclass
from BETinho.domain.event_result import EventResult


@dataclass
class Bet:
    event_id: str
    amount: float
    result: EventResult
    
    # TODO: add other fields as necessary

    def is_home_win(self):
        return self.result == EventResult.HOME_WIN

    def is_away_win(self):
        return self.result == EventResult.AWAY_WIN
    
    def is_draw(self):
        return self.result == EventResult.DRAW
