from datetime import datetime
import json
import unittest
from unittest.mock import Mock
import uuid

import dateutil
from django.conf import settings

from BETinho.betinho.domain.event.event_request import EventRequest
from BETinho.betinho.application.views.bet_view import BetView
from BETinho.betinho.domain.event.event_result import EventResult


class TestBetView(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        if not settings.configured:
            settings.configure(DEFAULT_CHARSET='UTF-8')
        self.event_id = str(uuid.uuid4())

    def _get_default_body(self):
        return {
            'event_id': self.event_id,
            'amount': 10.5,
            'result': EventResult.HOME_WIN,
        }

    def setUp(self):
        self.bet_maker = Mock()
        self.bet_view = BetView(self.bet_maker)

    def test_post_request_with_invalid_uuid_returns_400(self):
        body = self._get_default_body()
        request = Mock()
        request.body = json.dumps(body)

        response = self.bet_view.post(request, event_id='invalid_uuid')

        self.assertEqual(400, response.status_code)

    def test_post_request_without_amount_returns_400(self):
        body = {
            'event_id': self.event_id,
            'result': EventResult.HOME_WIN,
        }
        request = Mock()
        request.body = json.dumps(body)

        response = self.bet_view.post(request, event_id=self.event_id)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Bet amount is missing', 'The only valid request body keys are "amount" and "result"']
        }, json.loads(response.content))

    def test_post_request_amount_not_number_returns_400(self):
        body = {
            'amount': "invalid",
            'event_id': self.event_id,
            'result': EventResult.HOME_WIN,
        }
        request = Mock()
        request.body = json.dumps(body)

        response = self.bet_view.post(request, event_id=self.event_id)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Bet amount should be a number', 'The only valid request body keys are "amount" and "result"']
        }, json.loads(response.content))

    def test_post_request_missing_result_returns_400(self):
        body = {
            'amount': 10.5,
            'event_id': self.event_id,
        }
        request = Mock()
        request.body = json.dumps(body)

        response = self.bet_view.post(request, event_id=self.event_id)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Bet result is missing', 'The only valid request body keys are "amount" and "result"']
        }, json.loads(response.content))

    def test_post_request_invalid_result_returns_400(self):
        body = {
            'amount': 10.5,
            'event_id': self.event_id,
            'result': "invalid",
        }
        request = Mock()
        request.body = json.dumps(body)

        response = self.bet_view.post(request, event_id=self.event_id)

        self.assertEqual(400, response.status_code)
        self.assertEqual({
            'errors': ['Bet result should be an integer between 1 and 3. 1 = HOME_WIN, 2 = DRAW, 3 = AWAY_WIN', 'The only valid request body keys are "amount" and "result"']
        }, json.loads(response.content))
