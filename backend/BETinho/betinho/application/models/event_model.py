import uuid
from django.db import models

from BETinho.betinho.application.models.event_result_model import EventResultModel
from BETinho.betinho.application.models.team_model import TeamModel
from BETinho.betinho.domain.event import Event

class EventModel(models.Model):
    class Meta:
        db_table = 'event'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_team = models.ForeignKey('TeamModel', on_delete=models.CASCADE, related_name='+')
    away_team = models.ForeignKey('TeamModel', on_delete=models.CASCADE, related_name='+')
    description = models.TextField()
    start = models.DateTimeField()
    location = models.TextField()
    result = models.IntegerField(choices=EventResultModel.choices, null=True)

    @classmethod
    def from_event(cls, event: Event):
        id = event.event_id if event.event_id else uuid.uuid4()
        event_model = cls(
            id=id,
            home_team_id=event.home_team.id, 
            away_team_id=event.away_team.id, 
            description=event.description, 
            start=event.start, 
            location=event.location
        )

        return event_model

    def to_event(self) -> Event:
        return Event(
            event_id = self.id,
            home_team = TeamModel.to_team(self.home_team),
            away_team = TeamModel.to_team(self.away_team),
            description = self.description,
            start = self.start,
            location = self.location,
            result = self.result
        )
