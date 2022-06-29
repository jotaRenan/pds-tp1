import uuid
import json
from django.test import TestCase, Client

class BetIntegrationTest(TestCase):
    def setUp(self) -> None:
        pass


    def test_odds_fetching(self):
        client = Client()
        client.post('/events/register/', {'home_team': 'Cruzeiro',
                'away_team': 'Flamengo',
                'description': 'Cruzeiro x Flamengo',
                'start': '2020-01-01T00:00:00Z',
                'location': 'São Paulo'
            }, content_type='application/json')

        response = client.get('/events/')
        body = json.loads(response.content)
        event_id = body[0]['event_id']

        response = client.post(f'/events/{event_id}/bets/', {'amount' : 10, 
                'result' : 1
            }, content_type='application/json')
        response = client.post(f'/events/{event_id}/bets/', {'amount' : 10, 
                'result' : 3
            }, content_type='application/json')

        response = client.get(f'/events/{event_id}/odds/')
        body = json.loads(response.content)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(body['home'], body['away'])




    def test_odds_fetching_event_with_no_bets(self):
        client = Client()
        client.post('/events/register/', {'home_team': 'Cruzeiro',
                'away_team': 'Flamengo',
                'description': 'Cruzeiro x Flamengo',
                'start': '2020-01-01T00:00:00Z',
                'location': 'São Paulo'
            }, content_type='application/json')

        response = client.get('/events/')
        body = json.loads(response.content)
        event_id = body[0]['event_id']

        response = client.get(f'/events/{event_id}/odds/')
        self.assertEqual(response.status_code, 404)

