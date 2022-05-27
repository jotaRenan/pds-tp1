from BETinho.betinho.domain.event_repository import EventRepository
from BETinho.betinho.domain.event_fetcher import EventFetcher
from BETinho.betinho.domain.event import Event

class EventService(EventFetcher):

    def __init__(self, event_repository: EventRepository) -> None:
        self.event_repository = event_repository

    def get_event(self, event_id: str) -> Event:
        return self.event_repository.get_event_by_id(event_id)
