import dataclasses
import uuid

from django.views import View
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from BETinho.betinho.domain.odds_fetcher import OddsFetcher

class OddsView(View):
    odds_fetcher: OddsFetcher = None

    def __init__(self, odds_fetcher: OddsFetcher) -> None:
        self.odds_fetcher = odds_fetcher

    def get(self, _request, event_id: str):
        try:
            event_id_uuid = uuid.UUID(event_id)
        except ValueError:
            return JsonResponse({
                'message': f'Provided event_id {event_id} is not a valid UUID' 
            }, status=400)

    
        odds = self.odds_fetcher.get_odds_for_event(event_id_uuid)
        if odds is None:
            return JsonResponse({
            'message': f'Event {event_id} has no bets'
        }, status=404)

        json = dataclasses.asdict(odds)
        return JsonResponse(json, encoder=DjangoJSONEncoder)
