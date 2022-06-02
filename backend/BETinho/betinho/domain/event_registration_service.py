from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from BETinho.betinho.domain.event import Event

class EventRegistrationService(ABC):

    @abstractmethod
    def create_event(self, event: Event) -> None:
        pass