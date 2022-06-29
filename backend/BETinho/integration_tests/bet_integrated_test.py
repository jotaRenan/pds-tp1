import uuid
import json
from django.test import TestCase, Client

class BetIntegrationTest(TestCase):
    def setUp(self) -> None:
        pass


    def test_bet_creation_invalid_event_id(self):
        client = Client()
        event_id = uuid.uuid4()

        response = client.post(f'/events/{event_id}/bets/', {'amount' : 10, 
                'result' : 1
            }, content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_bet_creation(self):
        client = Client()
        client.post('/events/register/', {'home_team': 'Cruzeiro',
                'away_team': 'Flamengo',
                'description': 'Cruzeiro x Flamengo',
                'start': '2020-01-01T00:00:00Z',
                'location': 'São Paulo'
            }, content_type='application/json')

        response = client.get('/events/')
        self.assertEqual(response.status_code, 200)

        body = json.loads(response.content)
        event_id = body[0]['event_id']

        response = client.post(f'/events/{event_id}/bets/', {'amount' : 10, 
                'result' : 1
            }, content_type='application/json')
        self.assertEqual(response.status_code, 204)
