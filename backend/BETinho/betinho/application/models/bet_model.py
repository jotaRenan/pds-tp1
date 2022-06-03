import uuid
from django.db import models

from BETinho.betinho.application.models.event_result_model import EventResultModel
from BETinho.betinho.domain.event.bet.bet import Bet
from BETinho.betinho.domain.event.event_result import EventResult

class BetModel(models.Model):
    class Meta:
        db_table = 'bet'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey('EventModel', on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(decimal_places=2, max_digits=30)
    result = models.IntegerField(choices=EventResultModel.choices)

    @classmethod
    def from_bet(cls, bet: Bet):
        id = bet.id if bet.id else uuid.uuid4()
        bet_model = cls(
            id=id,
            event_id=bet.event_id, 
            amount=bet.amount, 
            result=bet.result.value
        )

        return bet_model

    def to_bet(self) -> Bet:
        return Bet(
            self.id,
            self.event_id,
            self.amount,
            EventResult(self.result)
        )
