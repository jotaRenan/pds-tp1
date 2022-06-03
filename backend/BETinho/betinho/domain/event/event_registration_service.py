from abc import ABC, abstractmethod

from BETinho.betinho.domain.event.event import Event

class EventRegistrationService(ABC):

    @abstractmethod
    def create_event(self, event: Event) -> None:
        pass
