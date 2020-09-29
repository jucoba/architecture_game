import unittest
from src.game.team import Team


class TestTeams(unittest.TestCase):

    def setUp(self) -> None:
        self.a_team = Team('A Team', 'Anibal')

    def test_create_team_name_must_be_set(self):
        self.assertEqual(self.a_team.team_name, 'A Team')

    def test_create_team_balance_must_be_set(self):
        self.assertEqual(self.a_team.balance, 100000)

    def test_create_team_architecture_level_must_be_set(self):
        self.assertEqual(self.a_team.architecture_level, 1)

    def test_create_team_can_receive_new_clients_must_be_set(self):
        self.assertEqual(self.a_team.can_receive_new_clients, False)

    def test_create_team_must_have_0_capacity(self):
        self.assertEqual(self.a_team.capacity, 100)

    def test_create_team_must_have_a_4_digit_id(self):
        self.assertGreaterEqual(self.a_team.id, 1000)
        self.assertLessEqual(self.a_team.id, 9999)

    def test_create_team_must_have_0_clients(self):
        self.assertEqual(self.a_team.current_clients, 0)
