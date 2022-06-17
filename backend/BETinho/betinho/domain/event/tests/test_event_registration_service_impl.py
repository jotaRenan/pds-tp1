import unittest
from unittest.mock import MagicMock, Mock
from datetime import datetime

from BETinho.betinho.domain.event.event_registration_service_impl import EventRegistrationServiceImpl
from BETinho.betinho.domain.event.event_request import EventRequest
from BETinho.betinho.domain.event.event import Event
from BETinho.betinho.domain.team.team import Team

class TestEventRegistrationServiceImpl(unittest.TestCase):
    def setUp(self) -> None:
        self.event_repository_mock = MagicMock()
        self.event_repository_mock.save = Mock()
        self.team_repository_mock = MagicMock()
        self.team_repository_mock.save = Mock()
        self.registration_service = EventRegistrationServiceImpl(self.event_repository_mock, self.team_repository_mock)


    def test_when_team_does_not_exist_then_team_is_created(self):
        request = EventRequest(
            home_team_name='home',
            away_team_name='away',
            description='description',
            start=datetime(2022, 2, 22),
            location='location'
        )
        self.team_repository_mock.get_team_by_name = Mock(return_value=None)
        self.registration_service.create_event(request)
        
        self.assertEqual(2, self.team_repository_mock.save.call_count)


    def test_when_team_exists_then_team_is_not_created(self):
        request = EventRequest(
            home_team_name='home',
            away_team_name='away',
            description='description',
            start=datetime(2022, 2, 22),
            location='location'
        )
        self.registration_service.create_event(request)
        self.team_repository_mock.get_team_by_name = Mock(return_value=Team(None, None))
        self.team_repository_mock.save.assert_not_called()

    
    def test_creates_event_with_correct_teams(self):
        request = EventRequest(
            home_team_name='home',
            away_team_name='away',
            description='description',
            start=datetime(2022, 2, 22),
            location='location'
        )
        self.team_repository_mock.get_team_by_name = Mock(return_value=Team('a', 'b'))
        self.registration_service.create_event(request)

        event = Event(
            event_id=None,
            home_team=Team('a', 'b'),
            away_team=Team('a', 'b'),
            description=request.description,
            start=request.start,
            location=request.location
        )

        self.event_repository_mock.save.assert_called_once_with(event)