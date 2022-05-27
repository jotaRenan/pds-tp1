import uuid
from django.db import models

from BETinho.betinho.application.models.event_result_model import EventResultModel

class BetModel(models.Model):
    class Meta:
        db_table = 'bet'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey('EventModel', on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(decimal_places=2, max_digits=30)
    result = models.IntegerField(choices=EventResultModel.choices)
