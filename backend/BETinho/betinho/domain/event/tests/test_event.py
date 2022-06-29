import datetime
from unittest import TestCase
import uuid

from BETinho.betinho.domain.event.event import Event
from BETinho.betinho.domain.event.event_result import EventResult
from BETinho.betinho.domain.team.team import Team


class TestEvent(TestCase):
    
    def test_when_result_is_not_none_is_finished_returns_true(self):
        event = Event(
            event_id=uuid.uuid4(),
            home_team=Team(uuid.uuid4(), 'Brasil'),
            away_team=Team(uuid.uuid4(), 'Argentina'),
            description='MyEvent',
            start=datetime.datetime(2022, 2, 22),
            location='somewhere',
            result=EventResult.HOME_WIN
        )
        self.assertTrue(event.is_finished())

    def test_when_result_is_none_is_finished_returns_false(self):
        event = Event(
            event_id=uuid.uuid4(),
            home_team=Team(uuid.uuid4(), 'Brasil'),
            away_team=Team(uuid.uuid4(), 'Argentina'),
            description='MyEvent',
            start=datetime.datetime(2022, 2, 22),
            location='somewhere',
            result=None
        )
        self.assertFalse(event.is_finished())
    
    def test_when_result_is_home_win_is_home_win_returns_true(self):
        event = Event(
            event_id=uuid.uuid4(),
            home_team=Team(uuid.uuid4(), 'Brasil'),
            away_team=Team(uuid.uuid4(), 'Argentina'),
            description='MyEvent',
            start=datetime.datetime(2022, 2, 22),
            location='somewhere',
            result=EventResult.HOME_WIN
        )

        self.assertTrue(event.is_home_win())
        self.assertFalse(event.is_away_win())
        self.assertFalse(event.is_draw())

    def test_when_result_is_away_win_is_away_win_returns_true(self):
        event = Event(
            event_id=uuid.uuid4(),
            home_team=Team(uuid.uuid4(), 'Brasil'),
            away_team=Team(uuid.uuid4(), 'Argentina'),
            description='MyEvent',
            start=datetime.datetime(2022, 2, 22),
            location='somewhere',
            result=EventResult.AWAY_WIN
        )
        
        self.assertTrue(event.is_away_win())
        self.assertFalse(event.is_home_win())
        self.assertFalse(event.is_draw())
    
    def test_when_result_is_draw_is_draw_returns_true(self):
        event = Event(
            event_id=uuid.uuid4(),
            home_team=Team(uuid.uuid4(), 'Brasil'),
            away_team=Team(uuid.uuid4(), 'Argentina'),
            description='MyEvent',
            start=datetime.datetime(2022, 2, 22),
            location='somewhere',
            result=EventResult.DRAW
        )
        
        self.assertTrue(event.is_draw())
        self.assertFalse(event.is_home_win())
        self.assertFalse(event.is_away_win())
