from BETinho.betinho.domain.team.team_repository import TeamRepository
from BETinho.betinho.domain.team.team import Team
from BETinho.betinho.application.models.team_model import TeamModel

class TeamRepositoryImpl(TeamRepository):

    def get_team_by_name(self, name: str) -> Team:
        print(f'Get team by name: {name}')

        try:
            team = TeamModel.objects.get(name=name)
        except TeamModel.DoesNotExist:
            return None
        return team.to_team()

    def save(self, team: Team) -> None:
        TeamModel.from_team(team).save()
