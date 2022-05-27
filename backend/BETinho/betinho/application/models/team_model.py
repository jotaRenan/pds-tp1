import uuid
from django.db import models

class TeamModel(models.Model):
    class Meta:
        db_table = 'team'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
