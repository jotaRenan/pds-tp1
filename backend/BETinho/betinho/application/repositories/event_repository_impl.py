from datetime import datetime
from uuid import UUID

from typing import Optional

from BETinho.betinho.domain.event_repository import EventRepository
from BETinho.betinho.application.models.event_model import EventModel
from BETinho.betinho.domain.event import Event

class EventRepositoryImpl(EventRepository):
    def get_event_by_id(self, event_id: UUID) -> Optional[Event]:
        print(f'Get event: {event_id}')

        try:
            event = EventModel.objects.get(pk=event_id)
        except EventModel.DoesNotExist:
            return None
        return event.to_event()
