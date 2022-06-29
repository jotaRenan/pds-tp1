import sys
import uuid
import unittest

from unittest.mock import Mock
from datetime import datetime

from BETinho.betinho.domain.team.team import Team

sys.modules['BETinho.betinho.application.models.team_model'] = Mock()

from BETinho.betinho.application.repositories.team_repository_impl import TeamRepositoryImpl

class TestTeamRepositoryImpl(unittest.TestCase):

    def setUp(self):
        self.mock_team_model_module = sys.modules['BETinho.betinho.application.models.team_model']
        self.team_repository = TeamRepositoryImpl()

    def test_save_calls_event_model_save(self):
        team = Team(uuid.uuid4(), "team")

        from_team_return_mock = Mock()
        from_team_return_mock.save = Mock()
        self.mock_team_model_module.TeamModel.from_team = Mock(
            return_value=from_team_return_mock)

        self.team_repository.save(team)

        from_team_return_mock.save.assert_called_once()
        self.mock_team_model_module.TeamModel.from_team.assert_called_once_with(
            team)
