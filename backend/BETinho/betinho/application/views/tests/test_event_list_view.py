from datetime import datetime
import unittest
from urllib import response
import uuid
import json
from unittest.mock import Mock

from django.conf import settings
from BETinho.betinho.application.views.event_list_view import EventListView
from BETinho.betinho.application.views.event_registration_view import EventRegistrationView
from BETinho.betinho.domain.event.event import Event
from BETinho.betinho.domain.team.team import Team


class TestEventListView(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        if not settings.configured:
            settings.configure(DEFAULT_CHARSET='UTF-8')

    def setUp(self):
        self.event_fetcher = Mock()
        self.event_list_view = EventListView(self.event_fetcher)

    def test_no_events_returns_http_204(self):
        self.event_fetcher.get_event_list = Mock(return_value=[])
        response = self.event_list_view.get(None)

        self.assertEqual(204, response.status_code)

    def test_has_events_returns_json_with_events(self):
        mock_event = Event(
                event_id=uuid.uuid4(),
                home_team=Team(team_id=uuid.uuid4(), name='Home Team'),
                away_team=Team(team_id=uuid.uuid4(), name='Away Team'),
                description='Event 1 description',
                start=datetime(2020, 1, 1),
                location='Event 1 location'
            )
        self.event_fetcher.get_event_list = Mock(return_value=[mock_event])

        response = self.event_list_view.get(None)
        self.assertEqual(200, response.status_code)
        self.assertEqual([
            {
                'event_id': str(mock_event.event_id),
                'home_team': {
                    'team_id': str(mock_event.home_team.team_id),
                    'name': mock_event.home_team.name
                },
                'away_team': {
                    'team_id': str(mock_event.away_team.team_id),
                    'name': mock_event.away_team.name
                },
                'description': mock_event.description,
                'start': mock_event.start.isoformat(),
                'location': mock_event.location,
                'result': None
            }
        ], json.loads(response.content))
