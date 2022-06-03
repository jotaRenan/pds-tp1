from decimal import Decimal
import json
from typing import List
import uuid

from django.views import View
from django.http import HttpResponse, JsonResponse

from BETinho.betinho.domain.event.bet.bet_service import BetRegistrationService
from BETinho.betinho.domain.event.bet.bet import Bet
from BETinho.betinho.domain.event.event_result import EventResult
from BETinho.betinho.domain.not_found_exception import NotFoundException

class BetView(View):
    bet_maker: BetRegistrationService = None

    def __init__(self, bet_maker: BetRegistrationService) -> None:
        self.bet_maker = bet_maker

    def post(self, request, event_id: str):
        try:
            event_id_uuid = uuid.UUID(event_id)
        except ValueError:
            return JsonResponse({
                'message': f'Provided event_id {event_id} is not a valid UUID' 
            }, status=400)
        
        body = json.loads(request.body)

        validation_errors = self.validate_request_body(body)
        
        if len(validation_errors) > 0:
            return JsonResponse({
                'errors': validation_errors
            }, status=400)
        
        bet_to_create = Bet(
            id=None,
            event_id=event_id_uuid,
            amount=Decimal(str(body['amount'])),
            result=EventResult(body['result'])
        )

        try:
            self.bet_maker.create_bet(bet_to_create)
        except NotFoundException as e:
            return JsonResponse({
                'message': str(e)
            }, status=400)

        return HttpResponse(status=204)

    def validate_request_body(self, body) -> List[str]:
        errors = []
        if 'amount' not in body:
            errors.append('Bet amount is missing')
        elif not isinstance(body['amount'], float) and not isinstance(body['amount'], int):
            errors.append('Bet amount should be a number')
        
        if 'result' not in body:
            errors.append('Bet result is missing')
        elif not isinstance(body['result'], int) or body['result'] not in [1, 2, 3]:
            errors.append('Bet result should be an integer between 1 and 3. 1 = HOME_WIN, 2 = DRAW, 3 = AWAY_WIN')

        if any(key not in ['amount', 'result'] for key in body.keys()):
            errors.append('The only valid request body keys are "amount" and "result"')
        return errors
