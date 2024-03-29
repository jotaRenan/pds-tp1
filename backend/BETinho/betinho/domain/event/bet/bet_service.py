from abc import ABC, abstractmethod

from BETinho.betinho.domain.event.bet.bet import Bet

class BetRegistrationService(ABC):

    @abstractmethod
    def create_bet(self, bet_to_create: Bet) -> None:
        pass
