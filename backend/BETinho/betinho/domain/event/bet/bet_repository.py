from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from BETinho.betinho.domain.event.bet.bet import Bet

class BetRepository(ABC):

    @abstractmethod
    def get_bets_by_event_id(self, event_id: UUID) -> List[Bet]:
        pass

    @abstractmethod
    def save(self, bet: Bet) -> None:
        pass
