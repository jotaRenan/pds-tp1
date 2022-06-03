import uuid
from django.db import models
from BETinho.betinho.domain.team.team import Team

class TeamModel(models.Model):
    class Meta:
        db_table = 'team'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    @classmethod
    def from_team(cls, team: Team):
        id = team.team_id if team.team_id else uuid.uuid4()
        team_model = cls(id=id, name=team.name)

        return team_model

    def to_team(self) -> Team:
        return Team(
            team_id = self.id,
            name = self.name
        )
