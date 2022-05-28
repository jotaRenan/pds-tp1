"""BETinho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from BETinho.betinho.application.views.odds_view import OddsView
from BETinho.betinho.domain.odds_service import OddsService
from BETinho.betinho.application.repositories.bet_repository_impl import BetRepositoryImpl
from BETinho.betinho.domain.odds_calculator import OddsCalculator

from BETinho.betinho.application.views.event_view import EventView
from BETinho.betinho.domain.event_service import EventService
from BETinho.betinho.application.repositories.event_repository_impl import EventRepositoryImpl

from BETinho.betinho.application.views.bet_view import BetView
from BETinho.betinho.domain.bet_service import BetService

from BETinho.betinho.application.models.bet_model import BetModel
from BETinho.betinho.application.models.event_model import EventModel
from BETinho.betinho.application.models.team_model import TeamModel

admin.autodiscover()
# admin.site.register(BetModel)
# admin.site.register(EventModel)
# admin.site.register(TeamModel)

# Manual DI

bet_repository = BetRepositoryImpl()
odds_calculator = OddsCalculator()
odds_fetcher = OddsService(bet_repository, odds_calculator)
odds_view = OddsView.as_view(odds_fetcher=odds_fetcher)

event_repository = EventRepositoryImpl()
event_fetcher = EventService(event_repository)
event_view = EventView.as_view(event_fetcher=event_fetcher)

bet_maker = BetService(bet_repository=bet_repository, event_repository=event_repository)
bet_view = BetView.as_view(bet_maker=bet_maker)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/<event_id>', event_view),
    path('events/<event_id>/odds', odds_view),
    path('events/<event_id>/bets', bet_view)
]
