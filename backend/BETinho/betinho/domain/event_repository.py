from abc import ABC, abstractmethod

from BETinho.betinho.domain.event import Event

class EventRepository(ABC):

    @abstractmethod
    def get_event_by_id(self, event_id: str) -> Event:
        pass
