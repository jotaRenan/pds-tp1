import uuid
from django.db import models
from BETinho.betinho.domain.team import Team

class TeamModel(models.Model):
    class Meta:
        db_table = 'team'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    def to_team(self) -> Team:
        return Team(
            team_id = str(self.id),
            name = self.name
        )
