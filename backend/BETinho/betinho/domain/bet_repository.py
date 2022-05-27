from abc import ABC, abstractmethod
from typing import List

from BETinho.betinho.domain.bet import Bet

class BetRepository(ABC):

    @abstractmethod
    def get_bets_by_event_id(self, event_id: str) -> List[Bet]:
        pass
