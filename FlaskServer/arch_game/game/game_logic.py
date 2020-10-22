from arch_game.game.team import Team
from arch_game.game.game_board import GameBoard
import random as rand


class GameLogic:

    def __init__(self):
        self.board = GameBoard()

    def register_new_team(self, team: Team):
        self.board.add_team(team)

    @property
    def teams(self):
        return self.board.teams

    def new_cicle(self, f_get_new_clients=None):
        for team in self.teams.values():
            if f_get_new_clients is not None:
                new_clients = f_get_new_clients
            else:
                new_clients = rand.choice(self.board.get_random_clients_low())
            team.add_clients(new_clients)



