from datetime import datetime
import unittest
from urllib import response
import uuid
import json
from unittest.mock import Mock

from django.conf import settings
from django.http import Http404

from BETinho.betinho.application.views.odds_view import OddsView

class TestOddsView(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        if not settings.configured:
            settings.configure(DEFAULT_CHARSET='UTF-8')

    def setUp(self):
        self.odds_fetcher = Mock()
        self.odds_view = OddsView(self.odds_fetcher)

    def test_get_request_returns_400(self):
        request = Mock()
        response = self.odds_view.get(request, 'invalid_uid')
        self.assertEqual(400, response.status_code)

    def test_get_request_returns_404(self):
        invalid_valid_uuid = str(uuid.uuid4())
        message = 'Event ' + invalid_valid_uuid + ' has no bets'
        self.odds_fetcher.get_odds_for_event = Mock(return_value=None)
        self.odds_fetcher.create_event.side_effect = Exception(message)
        request = Mock()
        response = self.odds_view.get(request, invalid_valid_uuid)
        self.assertEqual({
            'message': message
        }, json.loads(response.content))
