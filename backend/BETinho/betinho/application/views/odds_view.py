import dataclasses

from django.views import View
from django.http import JsonResponse

from BETinho.betinho.domain.odds_fetcher import OddsFetcher

class OddsView(View):
    odds_fetcher: OddsFetcher = None

    def __init__(self, odds_fetcher: OddsFetcher) -> None:
        self.odds_fetcher = odds_fetcher

    def get(self, _request, event_id: str):
        print(event_id)

        odds = self.odds_fetcher.get_odds_for_event(event_id)
        json = dataclasses.asdict(odds)

        return JsonResponse(json)
