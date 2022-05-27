from BETinho.betinho.domain.bet_repository import BetRepository
from BETinho.betinho.domain.event_odds import EventOdds
from BETinho.betinho.domain.event_bets_summary import EventBetsSummary
from BETinho.betinho.domain.odds_fetcher import OddsFetcher
from BETinho.betinho.domain.odds_calculator import OddsCalculator

class OddsService(OddsFetcher):

    def __init__(self, bet_repository: BetRepository, odds_calculator: OddsCalculator) -> None:
        self.bet_repository = bet_repository
        self.odds_calculator = odds_calculator

    def get_odds_for_event(self, event_id: str) -> EventOdds:
        bets = self.bet_repository.get_bets_by_event_id(event_id)
        summary = EventBetsSummary(bets)

        return self.odds_calculator.calculate_odds(summary)
