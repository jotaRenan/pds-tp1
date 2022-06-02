import dataclasses
import json
from dateutil import parser

from django.views import View
from django.http import HttpResponse, JsonResponse

from BETinho.betinho.domain.event_registration_service import EventRegistrationService
from BETinho.betinho.domain.event_request import EventRequest


class EventRegistrationView(View):
    event_maker: EventRegistrationService = None

    def __init__(self, event_maker: EventRegistrationService) -> None:
        self.event_maker = event_maker

    def post(self, _request):
        body = json.loads(_request.body)

        print(body)

        validation_errors = self.validate_request_body(body)

        if len(validation_errors) > 0:
            return JsonResponse({
                'errors': validation_errors
            }, status=400)
        
        event_request = EventRequest(
            home_team_name = body['home_team'],
            away_team_name = body['away_team'],
            description = body['description'],
            start = parser.isoparse(body['start']),
            location = body['location'],
        )

        try:
            self.event_maker.create_event(event_request)
        except Exception as e:
            return JsonResponse({
                'message': str(e)
            }, status=400)

        return HttpResponse(status=204)

    def validate_request_body(self, body):
        errors = []
        if 'home_team' not in body:
            errors.append('Home team name is missing')
        elif not isinstance(body['home_team'], str):
            errors.append('Home team should be a string')
        
        if 'away_team' not in body:
            errors.append('Away team name is missing')
        elif not isinstance(body['away_team'], str):
            errors.append('Away team should be a string')

        if 'description' not in body:
            errors.append('Description is missing')
        elif not isinstance(body['description'], str):
            errors.append('Description should be a string')
        
        if 'location' not in body:
            errors.append('Location name is missing')
        elif not isinstance(body['location'], str):
            errors.append('Location should be a string')

        if 'start' not in body:
            errors.append('Start date name is missing')
        else:
            try:
                _ = parser.isoparse(body['start'])
            except ValueError:
                errors.append('Start date should be in ISO 8601 format')


        if any(key not in ['home_team', 'away_team', 'description', 'start', 'location'] for key in body.keys()):
            errors.append('Invalid request body key')

        return errors
