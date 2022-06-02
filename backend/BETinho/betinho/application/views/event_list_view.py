import dataclasses

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from BETinho.betinho.domain.event_fetching_service import EventFetchingService

class EventListView(View):
    event_fetcher: EventFetchingService = None

    def __init__(self, event_fetcher: EventFetchingService) -> None:
        self.event_fetcher = event_fetcher

    def get(self, _request):
        events = self.event_fetcher.get_event_list()
        if len(events) == 0:
            raise HttpResponse(status=204)
        
        json = list(map(dataclasses.asdict, events))
        return JsonResponse(json, encoder=DjangoJSONEncoder, safe=False)
