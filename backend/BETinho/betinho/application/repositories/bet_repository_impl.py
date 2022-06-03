from typing import List
from uuid import UUID

from BETinho.betinho.domain.event.bet.bet_repository import BetRepository
from BETinho.betinho.domain.event.bet.bet import Bet
from BETinho.betinho.application.models.bet_model import BetModel

class BetRepositoryImpl(BetRepository):
    def get_bets_by_event_id(self, event_id: UUID) -> List[Bet]:
        print(f'Get bets by event id: {event_id}')

        bet_models = BetModel.objects.filter(event_id=event_id)
        
        return list(
            map(lambda bet_model: bet_model.to_bet(), bet_models)
        )

    def save(self, bet: Bet) -> None:
        BetModel.from_bet(bet).save()
