from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from BETinho.betinho.domain.event import Event

class EventFetcher(ABC):

    @abstractmethod
    def get_event(self, event_id: UUID) -> Optional[Event]:
        pass
