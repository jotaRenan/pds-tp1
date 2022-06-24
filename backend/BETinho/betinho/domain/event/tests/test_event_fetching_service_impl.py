import unittest
import uuid
from unittest.mock import MagicMock, Mock
from datetime import datetime

from BETinho.betinho.domain.event.event_fetching_service_impl import EventFetchingServiceImpl
from BETinho.betinho.domain.event.event import Event

class TestEventRegistrationServiceImpl(unittest.TestCase):
    def setUp(self) -> None:
        self.event_repository_mock = MagicMock()
        self.event_repository_mock.get_event_by_id = Mock()
        self.event_repository_mock.get_event_list = Mock()
        self.registration_service = EventFetchingServiceImpl(self.event_repository_mock)

    def test_get_event_returns_same_value_as_repository(self):
        event = Event(uuid.uuid4(), 'Cruzeiro', 'Corinthians', 'description', datetime(2022, 2, 22), 'location')
        self.event_repository_mock.get_event_by_id = Mock(return_value=event)
        self.assertEqual(self.registration_service.get_event(event), event)

        self.event_repository_mock.get_event_by_id.assert_called_once_with(event)
    
    def test_get_event_list_returns_same_value_as_repository(self):
        event_list = [
            Event(uuid.uuid4(), 'Cruzeiro', 'Corinthians', 'description', datetime(2022, 2, 22), 'Mineirão'),
            Event(uuid.uuid4(), 'São Paulo', 'Palmeiras', 'description', datetime(2022, 2, 23), 'Morumbi')
        ]
        self.event_repository_mock.get_event_list = Mock(return_value=event_list)
        self.assertEqual(self.registration_service.get_event_list(), event_list)
        self.event_repository_mock.get_event_list.assert_called_once()
