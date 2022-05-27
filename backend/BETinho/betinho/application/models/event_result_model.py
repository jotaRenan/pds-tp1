from django.db import models

class EventResultModel(models.IntegerChoices):
    HOME_WIN = 1
    DRAW = 2
    AWAY_WIN = 3
