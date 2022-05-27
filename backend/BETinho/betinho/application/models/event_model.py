import uuid
from django.db import models

from BETinho.betinho.application.models.event_result_model import EventResultModel

class EventModel(models.Model):
    id: models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_team: models.ForeignKey('Team', on_delete=models.CASCADE, related_name='+')
    away_team: models.ForeignKey('Team', on_delete=models.CASCADE, related_name='+')
    description: models.TextField()
    start: models.DateTimeField()
    location: models.TextField()
    result: models.IntegerField(choices=EventResultModel.choices, null=True)
