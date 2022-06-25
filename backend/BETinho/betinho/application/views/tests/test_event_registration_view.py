from datetime import datetime
import json
import unittest
from unittest.mock import Mock

import dateutil
from django.conf import settings

from BETinho.betinho.domain.event.event_request import EventRequest
from BETinho.betinho.application.views.event_registration_view import EventRegistrationView

class TestEventRegistrationView(unittest.TestCase):
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
        self.event_maker = Mock()
        self.event_registration_view = EventRegistrationView(self.event_maker)

    def test_post_request_with_valid_body_returns_204(self):
        body = self._get_default_body()
        request = Mock()
        request.body = json.dumps(body)

        response = self.event_registration_view.post(request)

        self.assertEqual(204, response.status_code)
        self.event_maker.create_event.assert_called_with(EventRequest(
            home_team_name = 'Cruzeiro',
            away_team_name = 'Corinthians',
            description = 'Jogo de volta da final da Copa do Brasil 2018',
            start = datetime(2018, 11, 5, 21, 30, 0, tzinfo=dateutil.tz.tzutc()),
            location = 'Mineirão'
        ))
    
    def test_event_registration_service_raises_returns_400_with_exception_message(self):
        body = self._get_default_body()
        request = Mock()
        request.body = json.dumps(body)

        self.event_maker.create_event.side_effect = Exception('MyCustomMockError')
        
        
        response = self.event_registration_view.post(request)
        self.assertEqual({
            'message': 'MyCustomMockError'
        }, json.loads(response.content))
    
    def test_post_request_missing_home_team_returns_400_with_expected_message(self):
        body = self._get_default_body()
        del body['home_team']

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)
        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Home team name is missing']
        }, json.loads(response.content))

    def test_post_request_missing_away_team_returns_400_with_expected_message(self):
        body = self._get_default_body()
        del body['away_team']

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Away team name is missing']
        }, json.loads(response.content))

    def test_post_request_missing_description_returns_400_with_expected_message(self):
        body = self._get_default_body()
        del body['description']

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Description is missing']
        }, json.loads(response.content))
    
    def test_post_request_description_not_a_string_returns_400_with_expected_message(self):
        body = self._get_default_body()
        body['description'] = True

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Description should be a string']
        }, json.loads(response.content))

    def test_post_request_missing_location_returns_400_with_expected_message(self):
        body = self._get_default_body()
        del body['location']

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Location name is missing']
        }, json.loads(response.content))

    def test_post_request_location_not_a_string_returns_400_with_expected_message(self):
        body = self._get_default_body()
        body['location'] = 1337

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Location should be a string']
        }, json.loads(response.content))

    def test_post_request_missing_start_returns_400_with_expected_message(self):
        body = self._get_default_body()
        del body['start']

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Start date is missing']
        }, json.loads(response.content))

    def test_post_request_start_not_a_iso8601_date_returns_400_with_expected_message(self):
        body = self._get_default_body()
        body['start'] = '01/01/2018'

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Start date should be in ISO 8601 format']
        }, json.loads(response.content))

    def test_post_request_unknown_keys_returns_400_with_expected_message(self):
        body = self._get_default_body()
        body['key1'] = 'value1'
        body['key2'] = 'value2'

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Invalid request body key']
        }, json.loads(response.content))

    def test_post_multiple_errors_returns_400_with_all_errors(self):
        body = self._get_default_body()
        del body['description']
        body['location'] = True
        body['key1'] = 'value1'
        body['key2'] = 'value2'

        request = Mock()
        request.body = json.dumps(body)
        response = self.event_registration_view.post(request)

        self.assertEqual(400, response.status_code)
        self.assertEqual(
            sorted([
                'Invalid request body key',
                'Location should be a string',
                'Description is missing'
            ]),
            sorted(json.loads(response.content)['errors'])
        )
