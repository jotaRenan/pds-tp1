from typing import Optional, List
from uuid import UUID

from BETinho.betinho.domain.event_repository import EventRepository
from BETinho.betinho.domain.event_fetching_service import EventFetchingService
from BETinho.betinho.domain.event import Event

class EventFetchingServiceImpl(EventFetchingService):

    def __init__(self, event_repository: EventRepository) -> None:
        self.event_repository = event_repository

    def get_event(self, event_id: UUID) -> Optional[Event]:
        return self.event_repository.get_event_by_id(event_id)

    def get_event_list(self) -> List[Event]:
        return self.event_repository.get_event_list()