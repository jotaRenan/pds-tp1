from datetime import datetime
import unittest
import uuid
from decimal import Decimal
from unittest.mock import Mock

from BETinho.betinho.domain.event.event import Event
from BETinho.betinho.domain.event.event import Team
from BETinho.betinho.domain.event.bet.bet import Bet
from BETinho.betinho.domain.event.bet.bet_service_impl import BetRegistrationServiceImpl
from BETinho.betinho.domain.not_found_exception import NotFoundException
from backend.BETinho.betinho.domain.event.event_result import EventResult

class TestBetRegistrationServiceImpl(unittest.TestCase):
    def setUp(self) -> None:
        self.bet_repository_mock = Mock()
        self.event_repository_mock = Mock()
        self.bet_service = BetRegistrationServiceImpl(self.bet_repository_mock, self.event_repository_mock)
    
    def test_create_bet_if_event_does_not_exist_then_throws_not_found_exception(self):
        unknown_event_id = uuid.uuid4()
        bet_to_create = Bet(uuid.uuid4(), unknown_event_id, Decimal('20.00'), EventResult.HOME_WIN)
        self.event_repository_mock.get_event_by_id = Mock(return_value=None)
        with self.assertRaises(NotFoundException):
            self.bet_service.create_bet(bet_to_create)
        
        self.event_repository_mock.get_event_by_id.assert_called_once_with(unknown_event_id)
        self.bet_repository_mock.save.assert_not_called()

    def test_create_bet_if_event_exists_then_calls_repository_save_with_argument(self):
        event_id = uuid.uuid4()
        bet_to_create = Bet(uuid.uuid4(), event_id, Decimal('20.00'), EventResult.HOME_WIN)

        event = Event(event_id, Team(uuid.uuid4(), 'Cruzeiro'),
            Team(uuid.uuid4(), 'Corinthians'), 'Random description',
            datetime(2022, 2, 22), 'Mineirão')
        
        self.event_repository_mock.get_event_by_id = Mock(return_value=event)
        self.bet_service.create_bet(bet_to_create)
        self.bet_repository_mock.save.assert_called_once_with(bet_to_create)
        self.event_repository_mock.get_event_by_id.assert_called_once_with(event_id)

