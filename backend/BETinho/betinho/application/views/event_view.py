import dataclasses
from uuid import UUID

from django.views import View
from django.http import JsonResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder

from BETinho.betinho.domain.event.event_fetching_service import EventFetchingService


class EventView(View):
    event_fetcher: EventFetchingService = None

    def __init__(self, event_fetcher: EventFetchingService) -> None:
        self.event_fetcher = event_fetcher

    def get(self, _request, event_id: str):
        try:
            event_id_uuid = UUID(event_id)
        except ValueError:
            return JsonResponse({
                'message': f'Provided event_id {event_id} is not a valid UUID' 
            }, status=400)

        event = self.event_fetcher.get_event(event_id_uuid)
        if event is None:
            raise Http404(f'Event {event_id} does not exist')
        
        json = dataclasses.asdict(event)        
        return JsonResponse(json, encoder=DjangoJSONEncoder)
