import unittest
from arch_game.game.game_board import GameBoard
from arch_game.game.team import Team


class TestGameBoard(unittest.TestCase):

    def test_new_board_must_have_0_teams(self):
        board = GameBoard()
        self.assertEqual(len(board.teams), 0)

    def test_when_add_a_team_to_new_board_must_have_1_teams(self):
        board = GameBoard()
        a_team = Team('A Team', 'Anibal')
        board.add_team(a_team)
        self.assertEqual(len(board.teams), 1)

    def test_when_add_two_teams_to_new_board_must_have_2_teams(self):
        board = GameBoard()
        a_team = Team('A Team', 'Anibal')
        p_team = Team('paw patrols', 'Ryder')
        board.add_team(a_team)
        board.add_team(p_team)
        self.assertEqual(len(board.teams), 2)

    def test_retrive_a_team_must_have_name_a_team(self):
        board = GameBoard()
        a_team = Team('A Team', 'Anibal')
        board.add_team(a_team)
        b_team = board.get_team(a_team.id)
        self.assertEqual(a_team, b_team)

    def test_create_random_clients(self):
        board = GameBoard()
        clients = board.get_random_clients_low()
        self.assertGreater(len(clients), 1)
