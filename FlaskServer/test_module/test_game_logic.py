import unittest
from arch_game.game.game_logic import GameLogic


class TestGameBoard(unittest.TestCase):

    def test_when_creating_new_team_board_must_have_one_team(self):
        game_logic: GameLogic = GameLogic()
        game_logic.register_new_team("A Team", "Anibal")
        self.assertEqual(len(game_logic.teams), 1)
