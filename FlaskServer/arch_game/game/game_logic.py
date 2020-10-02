from arch_game.game.team import Team
from arch_game.game.game_board import GameBoard


class GameLogic:

    def __init__(self):
        self.board = GameBoard()

    def register_new_team(self, team: Team):
        self.board.add_team(team)

    @property
    def teams(self):
        return self.board.teams
