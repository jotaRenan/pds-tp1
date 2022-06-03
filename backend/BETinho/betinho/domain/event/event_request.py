from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventRequest:
    home_team_name: str
    away_team_name: str
    description: str
    start: datetime
    location: str
