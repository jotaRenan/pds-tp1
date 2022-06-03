from uuid import UUID

from typing import Optional, List

from BETinho.betinho.domain.event.event_repository import EventRepository
from BETinho.betinho.application.models.event_model import EventModel
from BETinho.betinho.domain.event.event import Event

class EventRepositoryImpl(EventRepository):
    def get_event_by_id(self, event_id: UUID) -> Optional[Event]:
        print(f'Get event: {event_id}')

        try:
            event = EventModel.objects.get(pk=event_id)
        except EventModel.DoesNotExist:
            return None
        return event.to_event()

    def get_event_list(self) -> List[Event]:
        print(f'Get events')

        events = EventModel.objects.all()
        return [e.to_event() for e in events]

    def save(self, event: Event) -> None:
        print(event.home_team)
        print(event.away_team)
        EventModel.from_event(event).save()
