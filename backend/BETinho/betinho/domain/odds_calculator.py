from decimal import Decimal

from BETinho.betinho.domain.event_bets_summary import EventBetsSummary
from BETinho.betinho.domain.event_odds import EventOdds

class OddsCalculator:
    def calculate_odds(self, bets: EventBetsSummary) -> EventOdds:
        total_amount = bets.total_bet_amount()
        
        home_probability = self.calculate_probability(bets.total_amount_bet_on_home(), total_amount)
        away_probability = self.calculate_probability(bets.total_amount_bet_on_away(), total_amount)
        draw_probability = self.calculate_probability(bets.total_amount_bet_on_draw(), total_amount)

        return EventOdds(
            home=float(self.calculate_odd(home_probability)),
            away=float(self.calculate_odd(away_probability)),
            draw=float(self.calculate_odd(draw_probability))
        )

    def calculate_probability(self, amount_bet_on_result: Decimal, total_bet_amount: Decimal) -> Decimal:
        return amount_bet_on_result / total_bet_amount

    def calculate_odd(self, probability: Decimal) -> Decimal:
        if probability == Decimal(0):
            return 0
        return (Decimal(100) / probability) / Decimal(100)
