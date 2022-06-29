from datetime import datetime
import unittest
from urllib import response
import uuid
import json
from unittest.mock import Mock

from django.conf import settings
from django.http import Http404
from BETinho.betinho.application.views.event_list_view import EventListView
from BETinho.betinho.application.views.event_registration_view import EventRegistrationView

from BETinho.betinho.domain.event.event_request import EventRequest
from BETinho.betinho.application.views.event_view import EventView


class TestEventView(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        if not settings.configured:
            settings.configure(DEFAULT_CHARSET='UTF-8')

    def _get_default_body(self):
        return {
            'home_team': 'Cruzeiro',
            'away_team': 'Corinthians',
            'description': 'Jogo de volta da final da Copa do Brasil 2018',
            'start': '2018-11-05T21:30:00Z',
            'location': 'Mineirão'
        }

    def setUp(self):
        self.event_fetcher = Mock()
        self.event_view = EventView(self.event_fetcher)
        self.event_list_view = EventListView(self.event_fetcher)
        self.event_registration_view = EventRegistrationView(self.event_fetcher)

    def test_get_request_returns_400(self):
        request = Mock()
        response = self.event_view.get(request, 'invalid_uid')
        self.assertEqual(400, response.status_code)

    def test_get_request_returns_404(self):
        with self.assertRaises(Http404):
            self.event_fetcher.get_event = Mock(return_value=None)
            invalid_valid_uuid = str(uuid.uuid4())
            request = Mock()
            self.event_view.get(request, invalid_valid_uuid)

    def test_get_request_returns_204(self):
        # TODO
        # body = self._get_default_body()
        # registration_request = Mock()
        # registration_request.body = json.dumps(body)
        # list_request = Mock()
        # self.event_registration_view.post(registration_request)
        # self.event_fetcher.get_event_list = Mock(return_value=[self._get_default_body()])
        # response = self.event_list_view.get(list_request)
        # valid_id = json.loads(response.content)
        self.assertEqual(1, 1)

