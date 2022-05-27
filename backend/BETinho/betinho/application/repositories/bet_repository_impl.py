from typing import List
from BETinho.betinho.domain.bet_repository import BetRepository
from BETinho.betinho.domain.bet import Bet
from BETinho.betinho.domain.event_result import EventResult

class BetRepositoryImpl(BetRepository):
    def get_bets_by_event_id(self, event_id: str) -> List[Bet]:
        print(f'Get bets by event id: {event_id}')

        # TODO: implement actual database call using Django's ORM
        return [
            Bet(event_id, 8.00, EventResult.HOME_WIN),
            Bet(event_id, 1.00, EventResult.DRAW),
            Bet(event_id, 1.00, EventResult.AWAY_WIN),
        ]
