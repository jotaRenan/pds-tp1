from abc import ABC, abstractmethod

from BETinho.betinho.domain.event.event_request import EventRequest

class EventRegistrationService(ABC):

    @abstractmethod
    def create_event(self, event: EventRequest) -> None:
        pass
