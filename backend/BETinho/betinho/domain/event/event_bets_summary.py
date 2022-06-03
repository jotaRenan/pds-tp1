from decimal import Decimal
from typing import List, Tuple

from BETinho.betinho.domain.event.bet.bet import Bet

class EventBetsSummary:
    def __init__(self, bets: List[Bet]) -> None:
        (home, away, draw) = self.split_bets_by_result(bets)

        self.home = home
        self.away = away
        self.draw = draw

    def split_bets_by_result(self, bets: List[Bet]) -> Tuple[List[Bet], List[Bet], List[Bet]]:
        home = list(filter(lambda bet: bet.is_home_win(), bets))
        away = list(filter(lambda bet: bet.is_away_win(), bets))
        draw = list(filter(lambda bet: bet.is_draw(), bets))

        return (home, away, draw)

    def total_bet_amount(self) -> Decimal:
        return self.total_amount_bet_on_home() \
            + self.total_amount_bet_on_away() \
            + self.total_amount_bet_on_draw()
    
    def total_amount_bet_on_home(self) -> Decimal:
        return self._total_amount_bet_on_result(self.home)
    
    def total_amount_bet_on_away(self) -> Decimal:
        return self._total_amount_bet_on_result(self.away)
    
    def total_amount_bet_on_draw(self) -> Decimal:
        return self._total_amount_bet_on_result(self.draw)

    def _total_amount_bet_on_result(self, result: List[Bet]) -> Decimal:
        return sum(map(lambda bet: bet.amount, result))
