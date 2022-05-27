from abc import ABC, abstractmethod

from BETinho.betinho.domain.event import Event

class EventFetcher(ABC):

    @abstractmethod
    def get_event(self, event_id: str) -> Event:
        pass
