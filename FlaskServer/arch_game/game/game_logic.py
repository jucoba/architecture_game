from arch_game.game.team import Team
from arch_game.game.game_board import GameBoard


class GameLogic:

    def __init__(self):
        self.board = GameBoard()

    def register_new_team(self, team_name: str, player_name: str):
        t = Team(team_name, player_name)
        self.board.add_team(t)

    @property
    def teams(self):
        return self.board.teams
