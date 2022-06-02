from abc import ABC, abstractmethod

from BETinho.betinho.domain.team import Team

class TeamRepository(ABC):

    @abstractmethod
    def get_team_by_name(self, name: str) -> Team:
        pass

    @abstractmethod
    def save(self, team: Team) -> None:
        pass
