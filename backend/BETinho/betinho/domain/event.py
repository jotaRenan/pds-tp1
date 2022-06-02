from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from BETinho.betinho.domain.event_result import EventResult
from BETinho.betinho.domain.team import Team
from uuid import UUID


@dataclass
class Event:
    event_id: UUID
    home_team_id: UUID
    away_team_id: UUID
    description: str
    start: datetime
    location: str
    result: Optional[EventResult]

    def __init__(self, event_id, home_team_id, away_team_id, description, start, location, result=None):
        self.event_id = event_id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.description = description
        self.start = start
        self.location = location
        self.result = result

    def is_finished(self):
        return self.result is not None

    def is_home_win(self):
        return self.is_finished and self.result == EventResult.HOME_WIN

    def is_away_win(self):
        return self.is_finished and self.result == EventResult.AWAY_WIN
    
    def is_draw(self):
        return self.is_finished and self.result == EventResult.DRAW
