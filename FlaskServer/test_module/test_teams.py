import unittest
from src.dto.team import Team



class TestTeams(unittest.TestCase):


    def setUp(self) -> None:
        self.a_team = Team('A Team', 'Anibal')


    def test_create_team_name_must_be_set(self):
        self.assertEqual(self.a_team.name, 'A Team')

    def test_create_team_balance_must_be_set(self):
        self.assertEqual(self.a_team.balance, 100000)

    def test_create_team_architecture_level_must_be_set(self):
        self.assertEqual(self.a_team.architecture_level, 1)




