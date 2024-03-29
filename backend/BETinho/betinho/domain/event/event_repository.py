from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from BETinho.betinho.domain.event.event import Event

class EventRepository(ABC):

    @abstractmethod
    def get_event_by_id(self, event_id: UUID) -> Optional[Event]:
        pass

    @abstractmethod
    def get_event_list(self) -> List[Event]:
        pass

    @abstractmethod
    def save(self, event: Event) -> None:
        pass