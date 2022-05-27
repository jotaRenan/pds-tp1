import dataclasses
import uuid

from django.views import View
from django.http import JsonResponse

from BETinho.betinho.domain.odds_fetcher import OddsFetcher
from BETinho.betinho.domain.no_bets_exception import NoBetsException

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

        try:
            odds = self.odds_fetcher.get_odds_for_event(event_id_uuid)
            print(type(odds.home))
            json = dataclasses.asdict(odds)
            print(type(json['home']))

            return JsonResponse(json)
        except NoBetsException as e:
            return JsonResponse({
                'message': str(e)
            }, status=404)
