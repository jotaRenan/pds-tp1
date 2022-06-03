from BETinho.betinho.domain.event.event_repository import EventRepository
from BETinho.betinho.domain.team.team_repository import TeamRepository
from BETinho.betinho.domain.event.event_registration_service import EventRegistrationService
from BETinho.betinho.domain.event.event import Event
from BETinho.betinho.domain.event.event_request import EventRequest
from BETinho.betinho.domain.team.team import Team

class EventRegistrationServiceImpl(EventRegistrationService):

    def __init__(self, event_repository: EventRepository, team_repository : TeamRepository) -> None:
        self.event_repository = event_repository
        self.team_repository = team_repository

    def create_event(self, event_request: EventRequest) -> None:
        home_team = self.team_repository.get_team_by_name(event_request.home_team_name)
        if not home_team:
            self.team_repository.save(Team(None, event_request.home_team_name))
            home_team = self.team_repository.get_team_by_name(event_request.home_team_name)
        
        away_team = self.team_repository.get_team_by_name(event_request.away_team_name)
        if not away_team:
            self.team_repository.save(Team(None, event_request.away_team_name))
            away_team = self.team_repository.get_team_by_name(event_request.away_team_name)

        event = Event(
            event_id = None,
            home_team = home_team,
            away_team = away_team,
            description = event_request.description,
            start = event_request.start,
            location = event_request.location,
            result = None
        )

        return self.event_repository.save(event)
