from abc import ABC, abstractmethod
from uuid import UUID

from BETinho.betinho.domain.event import Event

class EventRepository(ABC):

    @abstractmethod
    def get_event_by_id(self, event_id: UUID) -> Event:
        pass
