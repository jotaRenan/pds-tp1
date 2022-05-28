from BETinho.betinho.domain.bet_maker import BetMaker
from BETinho.betinho.domain.bet_repository import BetRepository
from BETinho.betinho.domain.bet import Bet


class BetService(BetMaker):
    def __init__(self, bet_repository: BetRepository) -> None:
        self.bet_repository = bet_repository

    def create_bet(self, bet_to_create: Bet) -> None:
        self.bet_repository.save(bet_to_create)
