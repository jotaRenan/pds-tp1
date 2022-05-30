import dataclasses

from django.views import View
from django.http import JsonResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder

from BETinho.betinho.domain.event_fetcher import EventFetcher


class EventListView(View):
    event_fetcher: EventFetcher = None

    def __init__(self, event_fetcher: EventFetcher) -> None:
        self.event_fetcher = event_fetcher

    def get(self, _request):
        events = self.event_fetcher.get_event_list()
        if len(events) == 0:
            raise HttpResponse(status=204)
        
        json = list(map(dataclasses.asdict, events))
        return JsonResponse(json, encoder=DjangoJSONEncoder, safe=False)
