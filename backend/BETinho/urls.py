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
from BETinho.betinho.domain.event.odds.odds_fetching_service_impl import OddsFetchingServiceImpl
from BETinho.betinho.application.repositories.bet_repository_impl import BetRepositoryImpl
from BETinho.betinho.domain.event.odds.odds_calculator import OddsCalculator

from BETinho.betinho.application.views.event_view import EventView
from BETinho.betinho.application.views.event_list_view import EventListView
from BETinho.betinho.application.views.event_registration_view import EventRegistrationView
from BETinho.betinho.domain.event.event_fetching_service_impl import EventFetchingServiceImpl
from BETinho.betinho.domain.event.event_registration_service_impl import EventRegistrationServiceImpl
from BETinho.betinho.application.repositories.event_repository_impl import EventRepositoryImpl


from BETinho.betinho.application.repositories.team_repository_impl import TeamRepositoryImpl


from BETinho.betinho.application.views.bet_view import BetView
from BETinho.betinho.domain.event.bet.bet_service_impl import BetRegistrationServiceImpl

admin.autodiscover()
# admin.site.register(BetModel)
# admin.site.register(EventModel)
# admin.site.register(TeamModel)

# Manual DI

bet_repository = BetRepositoryImpl()
odds_calculator = OddsCalculator()
odds_fetcher = OddsFetchingServiceImpl(bet_repository, odds_calculator)
odds_view = OddsView.as_view(odds_fetcher=odds_fetcher)

event_repository = EventRepositoryImpl()
event_fetcher = EventFetchingServiceImpl(event_repository)
event_view = EventView.as_view(event_fetcher=event_fetcher)
event_list_view = EventListView.as_view(event_fetcher=event_fetcher)

team_repository = TeamRepositoryImpl()
event_maker = EventRegistrationServiceImpl(event_repository=event_repository, team_repository=team_repository)
event_registration_view = EventRegistrationView.as_view(event_maker=event_maker)

bet_registration_service = BetRegistrationServiceImpl(bet_repository=bet_repository, event_repository=event_repository)
bet_view = BetView.as_view(bet_maker=bet_registration_service)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', event_list_view),
    path('events/register/', event_registration_view),
    path('events/<event_id>/', event_view),
    path('events/<event_id>/odds/', odds_view),
    path('events/<event_id>/bets/', bet_view)
]
