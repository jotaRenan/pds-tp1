from datetime import datetime
import unittest
import uuid
from unittest.mock import Mock

from django.conf import settings

from BETinho.betinho.domain.event.event_request import EventRequest
from BETinho.betinho.application.views.event_view import EventView


class TestEventView(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        if not settings.configured:
            settings.configure(DEFAULT_CHARSET='UTF-8')

    def setUp(self):
        self.event_maker = Mock()
        self.event_view = EventView(self.event_maker)

    def test_get_request_returns_400(self):
        request = Mock()
        response = self.event_view.get(request, 'invalid_uid')
        self.assertEqual(400, response.status_code)

    def test_get_request_returns_404(self):
        # NOT WORKING
        request = Mock()
        response = self.event_view.get(request, str(uuid.uuid4()))
        self.assertEqual(404, response.status_code)

    def test_get_request_returns_204(self):
        # TODO
        self.assertEqual(1, 1)

