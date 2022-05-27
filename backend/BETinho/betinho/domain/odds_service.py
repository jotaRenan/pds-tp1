from uuid import UUID

from BETinho.betinho.domain.bet_repository import BetRepository
from BETinho.betinho.domain.event_odds import EventOdds
from BETinho.betinho.domain.event_bets_summary import EventBetsSummary
from BETinho.betinho.domain.no_bets_exception import NoBetsException
from BETinho.betinho.domain.odds_fetcher import OddsFetcher
from BETinho.betinho.domain.odds_calculator import OddsCalculator

class OddsService(OddsFetcher):

    def __init__(self, bet_repository: BetRepository, odds_calculator: OddsCalculator) -> None:
        self.bet_repository = bet_repository
        self.odds_calculator = odds_calculator

    def get_odds_for_event(self, event_id: UUID) -> EventOdds:
        bets = self.bet_repository.get_bets_by_event_id(event_id)
        if len(bets) == 0:
            raise NoBetsException(f'Event {event_id} has no bets')

        summary = EventBetsSummary(bets)

        return self.odds_calculator.calculate_odds(summary)
