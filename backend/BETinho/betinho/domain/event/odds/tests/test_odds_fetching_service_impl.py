import unittest
import uuid
from decimal import Decimal
from unittest.mock import Mock

from BETinho.betinho.domain.event.bet.bet import Bet
from BETinho.betinho.domain.event.event_result import EventResult
from BETinho.betinho.domain.event.odds.odds_fetching_service_impl import OddsFetchingServiceImpl
from backend.BETinho.betinho.domain.event.event_odds import EventOdds

class TestOddsFetchingServiceImpl(unittest.TestCase):
    def setUp(self) -> None:
        self.bet_repository_mock = Mock()
        self.odds_calculator_mock = Mock()
        self.bet_service = OddsFetchingServiceImpl(self.bet_repository_mock, self.odds_calculator_mock)
    
    def test_get_odds_for_event_if_no_bets_then_returns_none(self):
        event_id = uuid.uuid4()
        self.bet_repository_mock.get_bets_by_event_id = Mock(return_value=[])

        self.assertIsNone(self.bet_service.get_odds_for_event(event_id))
        self.bet_repository_mock.get_bets_by_event_id.assert_called_once_with(event_id)
        self.odds_calculator_mock.calculate_odds.assert_not_called()

    def test_get_odds_for_event_if_bet_list_is_not_empty_then_calls_odds_calculator_with_bets(self):
        event_id = uuid.uuid4()
        
        bet_1 = Bet(uuid.uuid4(), event_id, Decimal('20.00'), EventResult.HOME_WIN)
        bet_2 = Bet(uuid.uuid4(), event_id, Decimal('20.00'), EventResult.AWAY_WIN)
        bet_3 = Bet(uuid.uuid4(), event_id, Decimal('10.00'), EventResult.DRAW)

        self.bet_repository_mock.get_bets_by_event_id = Mock(return_value=[bet_1, bet_2, bet_3])
        self.odds_calculator_mock.calculate_odds = Mock(return_value=EventOdds(1.5, 1.5, 2.0))

        self.assertEqual(EventOdds(1.5, 1.5, 2.0), self.bet_service.get_odds_for_event(event_id))
        self.bet_repository_mock.get_bets_by_event_id.assert_called_once_with(event_id)

        self.odds_calculator_mock.calculate_odds.assert_called_once()
