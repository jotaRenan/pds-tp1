import sys
import uuid
import unittest
from unittest.mock import Mock
from decimal import Decimal

from BETinho.betinho.domain.event.bet.bet import Bet
from BETinho.betinho.domain.event.event_result import EventResult

sys.modules['BETinho.betinho.application.models.bet_model'] = Mock()

from BETinho.betinho.application.repositories.bet_repository_impl import BetRepositoryImpl

class TestBetRepositoryImpl(unittest.TestCase):
    
    def setUp(self):
        self.mock_bet_model_module = sys.modules['BETinho.betinho.application.models.bet_model']
        self.bet_repository = BetRepositoryImpl()

    def test_save_calls_bet_model_save(self):
        bet = Bet(uuid.uuid4(), uuid.uuid4(), Decimal(10), EventResult.AWAY_WIN)

        from_bet_return_mock = Mock()
        from_bet_return_mock.save = Mock()
        self.mock_bet_model_module.BetModel.from_bet = Mock(return_value=from_bet_return_mock)
        
        self.bet_repository.save(bet)

        from_bet_return_mock.save.assert_called_once()
        self.mock_bet_model_module.BetModel.from_bet.assert_called_once_with(bet)

