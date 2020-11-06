import unittest
from arch_game.game.game_logic import GameLogic
from arch_game.game.team import Team


class TestGameBoard(unittest.TestCase):

    def test_when_creating_new_team_board_must_have_one_team(self):
        game_logic: GameLogic = GameLogic()
        game_logic.register_new_team(Team("A Team", "Anibal"))
        self.assertEqual(len(game_logic.teams), 1)

    def test_get_team(self):
        game_logic: GameLogic = GameLogic()
        t = Team("A Team", "Anibal")
        game_logic.register_new_team(t)
        self.assertEqual(t, game_logic.teams[t.id])

    def mock_get_new_clients(self):
        return 50

    def test_new_cicle(self):
        game_logic: GameLogic = GameLogic()
        a = Team("A Team", "Anibal")
        b = Team("B Team", "Anibal")

        game_logic.register_new_team(a)
        game_logic.register_new_team(b)
        game_logic.new_cicle(self.mock_get_new_clients())

        self.assertEqual(50, a.current_clients)
        self.assertEqual(50, b.current_clients)
        self.assertEqual(97500, a.balance)
        self.assertEqual(97500, b.balance)




