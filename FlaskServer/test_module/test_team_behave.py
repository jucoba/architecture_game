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

    def test_team_capacity_with_arc_level_3_must_be_2000(self):
        a_team = self.create_new_team()
        a_team.architecture_level = 3
        self.assertEqual(a_team.capacity, 2000)

    def test_team_income_with_100_clients_must_be_5000(self):
        a_team = self.create_new_team()
        a_team.current_clients = 100
        self.assertEqual(a_team.income, 5000)

    def test_team_income_with_50_clients_must_be_2500(self):
        a_team = self.create_new_team()
        a_team.current_clients = 50
        self.assertEqual(a_team.income, 2500)

    def test_team_income_with_1_clients_must_be_50(self):
        a_team = self.create_new_team()
        a_team.current_clients = 1
        self.assertEqual(a_team.income, 50)

    def test_team_pyg_with_100_clients_and_arch_level_1_must_be_0(self):
        a_team = self.create_new_team()
        a_team.current_clients = 100
        a_team.architecture_level = 1
        self.assertEqual(a_team.pyg, 0)

    def test_team_pyg_with_600_clients_and_arch_level_2_must_be_15000(self):
        a_team = self.create_new_team()
        a_team.current_clients = 600
        a_team.architecture_level = 2
        self.assertEqual(a_team.pyg, 15000)

    def test_team_pyg_with_100_clients_and_arch_level_2_must_be_15000(self):
        a_team = self.create_new_team()
        a_team.current_clients = 100
        a_team.architecture_level = 2
        self.assertEqual(a_team.pyg, -10000)




