import json
from django.test import TestCase, Client

class EventIntegrationTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_event_creation(self):
        client = Client()

        response = client.get('/events/')
        self.assertEqual(response.status_code, 204)
        print(response)


        response = client.post('/events/register/', {'home_team': 'Cruzeiro',
                'away_team': 'Flamengo',
                'description': 'Cruzeiro x Flamengo',
                'start': '2020-01-01T00:00:00Z',
                'location': 'São Paulo'
            }, content_type='application/json')
        
        response = client.get('/events/')
        self.assertEqual(response.status_code, 200)

        body = json.loads(response.content)
        registered_event = body[0]
        self.assertEqual('Cruzeiro', registered_event['home_team']['name'])
        self.assertEqual('Flamengo', registered_event['away_team']['name'])
        self.assertEqual('Cruzeiro x Flamengo', registered_event['description'])
        self.assertEqual('São Paulo', registered_event['location'])
        self.assertEqual('2020-01-01T00:00:00Z', registered_event['start'])

