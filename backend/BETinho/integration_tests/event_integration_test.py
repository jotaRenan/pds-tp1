from django.test import TestCase, Client

from BETinho.betinho.application.views.event_list_view import EventListView

class EventIntegrationTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_event_creation(self):
        client = Client()

        response = client.get('/events/')
        self.assertEqual(response.status_code, 200)
        print(response)

        """
        response = client.post('/events/register/',
            {
                'home_team': 'Cruzeiro',
                'away_team': 'Flamengo',
                'description': 'Cruzeiro x Flamengo',
                'start': '2020-01-01T00:00:00Z',
                'location': 'São Paulo'
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['event'].name, 'Test Event')
        self.assertEqual(response.context['event'].description, 'Test Description')
        self.assertEqual(response.context['event'].date, '2020-01-01')
        """
        pass
