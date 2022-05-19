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

from BETinho.application.odds_view import OddsView
from BETinho.domain.odds_service import OddsService
from BETinho.application.bet_repository_impl import BetRepositoryImpl
from BETinho.domain.odds_calculator import OddsCalculator

# Manual DI

bet_repository = BetRepositoryImpl()
odds_calculator = OddsCalculator()
odds_fetcher = OddsService(bet_repository, odds_calculator)
odds_view = OddsView.as_view(odds_fetcher=odds_fetcher)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/<event_id>/odds', odds_view)
]
