import uuid

from BETinho.betinho.domain.bet_service import BetRegistrationService
from BETinho.betinho.domain.bet_repository import BetRepository
from BETinho.betinho.domain.bet import Bet
from BETinho.betinho.domain.event_repository import EventRepository
from BETinho.betinho.domain.not_found_exception import NotFoundException

class BetRegistrationServiceImpl(BetRegistrationService):
    def __init__(self, bet_repository: BetRepository, event_repository: EventRepository) -> None:
        self.bet_repository = bet_repository
        self.event_repository = event_repository

    def create_bet(self, bet_to_create: Bet) -> None:
        if self.event_repository.get_event_by_id(bet_to_create.event_id) is None:
            raise NotFoundException(f"Event with id {bet_to_create.event_id} does not exist")

        self.bet_repository.save(bet_to_create)
