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
            self.cicle_team(f_get_new_clients, team)

    def cicle_team(self, f_get_new_clients, team):
        if f_get_new_clients is not None:
            new_clients = f_get_new_clients
        else:
            while True:
                new_clients = int(rand.choice(self.board.get_random_clients_low()))
                if new_clients > 0:
                    break

        team.add_clients(new_clients)
        team.update_balance()

    def new_team_cicle(self, id, f_get_new_clients=None):
        team = self.board.get_team(id)
        self.cicle_team(f_get_new_clients, team)



