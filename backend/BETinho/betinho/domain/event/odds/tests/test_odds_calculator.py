from decimal import Decimal
import unittest
import uuid

from BETinho.betinho.domain.event.odds.odds_calculator import OddsCalculator
from BETinho.betinho.domain.event.bet.bet import Bet
from BETinho.betinho.domain.event.event_bets_summary import EventBetsSummary
from BETinho.betinho.domain.event.event_odds import EventOdds
from BETinho.betinho.domain.event.event_result import EventResult

class TestOddsCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = OddsCalculator()

    def test_when_bet_amount_on_each_result_is_equal_then_all_odds_are_three(self):
        event_id = uuid.uuid4()
        summary = EventBetsSummary([
            Bet(uuid.uuid4(), event_id, Decimal(10), EventResult.AWAY_WIN),
            Bet(uuid.uuid4(), event_id, Decimal(10), EventResult.DRAW),
            Bet(uuid.uuid4(), event_id, Decimal(10), EventResult.HOME_WIN)
        ])

        self.assertEqual(
            EventOdds(3.0, 3.0, 3.0),
            self.calculator.calculate_odds(summary)
        )
