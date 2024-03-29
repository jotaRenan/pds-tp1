from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from BETinho.betinho.domain.event.event_result import EventResult


@dataclass
class Bet:
    id: UUID
    event_id: UUID
    amount: Decimal
    result: EventResult
    
    # TODO: add other fields as necessary

    def is_home_win(self):
        return self.result == EventResult.HOME_WIN

    def is_away_win(self):
        return self.result == EventResult.AWAY_WIN
    
    def is_draw(self):
        return self.result == EventResult.DRAW
