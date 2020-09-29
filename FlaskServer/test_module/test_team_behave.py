import unittest
from src.game.team import Team


class TestTeamsBehave(unittest.TestCase):

    @staticmethod
    def create_new_team():
        a_team = Team('A Team', 'Anibal')
        return a_team

    def test_cicle_cost_arc_level_1_must_be_5000(self):
        a_team = self.create_new_team()
        a_team.architecture_level = 1
        self.assertEqual(a_team.cicle_cost, 5000)

    def test_cicle_cost_arc_level_2_must_be_15000(self):
        a_team = self.create_new_team()
        a_team.architecture_level = 2
        self.assertEqual(a_team.cicle_cost, 15000)

    def test_cicle_cost_arc_level_3_must_be_30000(self):
        a_team = self.create_new_team()
        a_team.architecture_level = 3
        self.assertEqual(a_team.cicle_cost, 30000)

    def test_team_capacity_with_arc_level_1_must_be_100(self):
        a_team = self.create_new_team()
        a_team.architecture_level = 1
        self.assertEqual(a_team.capacity, 100)

    def test_team_capacity_with_arc_level_2_must_be_600(self):
        a_team = self.create_new_team()
        a_team.architecture_level = 2
        self.assertEqual(a_team.capacity, 600)

    def test_team_capacity_with_arc_level_3_must_be_600(self):
        a_team = self.create_new_team()
        a_team.architecture_level = 3
        self.assertEqual(a_team.capacity, 2000)


