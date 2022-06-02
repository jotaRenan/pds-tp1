from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from BETinho.betinho.domain.event import Event

class EventFetchingService(ABC):

    @abstractmethod
    def get_event(self, event_id: UUID) -> Optional[Event]:
        pass

    @abstractmethod
    def get_event_list(self) -> List[Event]:
        pass