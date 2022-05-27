from BETinho.betinho.domain.event_repository import EventRepository
from BETinho.betinho.domain.event import Event

from BETinho.betinho.application.models.event_model import EventModel

from BETinho.betinho.domain.event_result import EventResult
from BETinho.betinho.domain.team import Team
from datetime import datetime

class EventRepositoryImpl(EventRepository):
    def get_event_by_id(self, event_id: str) -> Event:
        print(f'Get event: {event_id}')

        event = EventModel.objects.get(id=event_id)
        return event.to_event()

        # return Event(
        #     event_id=event_id,
        #     home_team=Team("0", "Team 0"),
        #     away_team=Team("1", "Team 1"),
        #     description="",
        #     start=datetime.now(),
        #     location="",
        #     result=EventResult.AWAY_WIN
        # )
