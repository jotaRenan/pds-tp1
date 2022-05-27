from abc import ABC, abstractmethod

from BETinho.betinho.domain.event_odds import EventOdds

class OddsFetcher(ABC):

    @abstractmethod
    def get_odds_for_event(self, event_id: str) -> EventOdds:
        pass
