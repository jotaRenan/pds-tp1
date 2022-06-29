import sys
import uuid
import unittest

from unittest.mock import Mock
from datetime import datetime

from BETinho.betinho.domain.event.event import Event
from BETinho.betinho.domain.event.event_result import EventResult
from BETinho.betinho.domain.team.team import Team

sys.modules['BETinho.betinho.application.models.event_model'] = Mock()

from BETinho.betinho.application.models.event_model import EventModel
from BETinho.betinho.application.repositories.event_repository_impl import EventRepositoryImpl

class TestEventRepositoryImpl(unittest.TestCase):

    def setUp(self):
        self.mock_event_model_module = sys.modules['BETinho.betinho.application.models.event_model']
        self.event_repository = EventRepositoryImpl()

    def test_get_event_by_id_fail(self):
        event_id = uuid.uuid4()
        EventModel.DoesNotExist = Exception
        
        self.mock_event_model_module.EventModel.objects.get = Mock(return_value=None)
        self.mock_event_model_module.EventModel.objects.get.side_effect = EventModel.DoesNotExist('Does not exist')
        
        actual = self.event_repository.get_event_by_id(event_id)

        self.assertIsNone(actual)

    def test_get_event_list(self):
        mock_event_model = Mock()

        expected_event = Event(
                uuid.uuid4(),
                Team(uuid.uuid4(), "Emelec"),
                Team(uuid.uuid4(), "Atlético"),
                "Oitavas Libertadores",
                datetime(2022, 6, 28),
                "Equador",
                EventResult.DRAW
            )
        mock_event_model.to_event = Mock(return_value=expected_event)
        self.mock_event_model_module.EventModel.objects.all = Mock(return_value=[mock_event_model])
        
        actual = self.event_repository.get_event_list()

        self.assertEqual([expected_event], actual)
        mock_event_model.to_event.assert_called_once()

    def test_save_calls_event_model_save(self):
        home_team = Team(uuid.uuid4(), "home_team")
        away_team = Team(uuid.uuid4(), "away_team")
        event = Event(uuid.uuid4(), home_team, away_team, "description", datetime(2022, 2, 22), "location", EventResult.AWAY_WIN)

        from_event_return_mock = Mock()
        from_event_return_mock.save = Mock()
        self.mock_event_model_module.EventModel.from_event = Mock(
            return_value=from_event_return_mock)

        self.event_repository.save(event)

        from_event_return_mock.save.assert_called_once()
        self.mock_event_model_module.EventModel.from_event.assert_called_once_with(
            event)
