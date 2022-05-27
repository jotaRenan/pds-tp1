import dataclasses

from django.views import View
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from BETinho.betinho.domain.event_fetcher import EventFetcher


class EventView(View):
    event_fetcher: EventFetcher = None

    def __init__(self, event_fetcher: EventFetcher) -> None:
        self.event_fetcher = event_fetcher

    def get(self, _request, event_id: str):
        print(event_id)

        event = self.event_fetcher.get_event(event_id)
        json = dataclasses.asdict(event)
        
        return JsonResponse(json, encoder=DjangoJSONEncoder)
