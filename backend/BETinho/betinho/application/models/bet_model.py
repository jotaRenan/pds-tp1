import uuid
from django.db import models

from BETinho.betinho.application.models.event_result_model import EventResultModel

class BetModel(models.Model):
    id: models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event: models.ForeignKey('Event', on_delete=models.CASCADE, related_name='+')
    amount: models.DecimalField(decimal_places=2)
    result: models.IntegerField(choices=EventResultModel.choices)
    a: models.TextField()
