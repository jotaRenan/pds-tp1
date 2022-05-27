from dataclasses import dataclass


@dataclass
class Team:
    team_id: str
    name: str

    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name
