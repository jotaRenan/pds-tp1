from typing import Optional
from uuid import UUID

from BETinho.betinho.domain.bet_repository import BetRepository
from BETinho.betinho.domain.event_odds import EventOdds
from BETinho.betinho.domain.event_bets_summary import EventBetsSummary
from BETinho.betinho.domain.odds_fetching_service import OddsFetchingService
from BETinho.betinho.domain.odds_calculator import OddsCalculator

class OddsFetchingServiceImpl(OddsFetchingService):

    def __init__(self, bet_repository: BetRepository, odds_calculator: OddsCalculator) -> None:
        self.bet_repository = bet_repository
        self.odds_calculator = odds_calculator

    def get_odds_for_event(self, event_id: UUID) -> Optional[EventOdds]:
        bets = self.bet_repository.get_bets_by_event_id(event_id)
        if len(bets) == 0:
            return None

        summary = EventBetsSummary(bets)

        return self.odds_calculator.calculate_odds(summary)
