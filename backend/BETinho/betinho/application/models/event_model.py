import uuid
from django.db import models

from BETinho.betinho.application.models.event_result_model import EventResultModel
from BETinho.betinho.domain.event import Event

class EventModel(models.Model):
    id: models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_team: models.ForeignKey('Team', on_delete=models.CASCADE, related_name='+')
    away_team: models.ForeignKey('Team', on_delete=models.CASCADE, related_name='+')
    description: models.TextField()
    start: models.DateTimeField()
    location: models.TextField()
    result: models.IntegerField(choices=EventResultModel.choices, null=True)

    def to_event(self) -> Event:
        return Event(
            event_id=str(self.id),
            home_team=home_team.to_team(),
            away_team=away_team.to_team(),
            description=self.description,
            start=self.start,
            location=self.location,
            result=self.result
        )
