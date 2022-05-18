from event_bets import EventBets
from event_odds import EventOdds

def calculate_odds(bets: EventBets) -> EventOdds:
    total_amount = bets.total_bet_amount()
    
    home_probability = calculate_probability(bets.total_amount_bet_on_home(), total_amount)
    away_probability = calculate_probability(bets.total_amount_bet_on_away(), total_amount)
    draw_probability = calculate_probability(bets.total_amount_bet_on_draw(), total_amount)

    return EventOdds(
        home=calculate_odd(home_probability),
        away=calculate_odd(away_probability),
        draw=calculate_odd(draw_probability)
    )

def calculate_probability(amount_bet_on_result, total_bet_amount) -> float:
    return amount_bet_on_result / total_bet_amount

def calculate_odd(probability) -> float:
    if probability == 0:
        return 0
    return (100 / probability) / 100
