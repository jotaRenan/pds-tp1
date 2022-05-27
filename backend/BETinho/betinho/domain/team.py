from dataclasses import dataclass
from uuid import UUID


@dataclass
class Team:
    team_id: UUID
    name: str

    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name
