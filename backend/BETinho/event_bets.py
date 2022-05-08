from typing import List
from bet import Bet


class EventBets:
    def __init__(self, home_bets: List[Bet], away_bets: List[Bet], draw_bets: List[Bet]):
        self.home = home_bets
        self.away = away_bets
        self.draw = draw_bets

    def total_bet_amount(self) -> float:
        return self.total_amount_bet_on_home() \
            + self.total_amount_bet_on_away() \
            + self.total_amount_bet_on_draw()
    
    def total_amount_bet_on_home(self) -> float:
        return self._total_amount_bet_on_result(self.home)
    
    def total_amount_bet_on_away(self) -> float:
        return self._total_amount_bet_on_result(self.away)
    
    def total_amount_bet_on_draw(self) -> float:
        return self._total_amount_bet_on_result(self.draw)

    def _total_amount_bet_on_result(self, result: List[Bet]) -> float:
        return sum(map(lambda bet: bet.amount, result))
