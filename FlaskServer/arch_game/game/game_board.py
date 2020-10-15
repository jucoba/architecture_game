from typing import Dict, Any
from arch_game.game.team import Team
import numpy as np


class GameBoard:
    teams: Dict[int, Team]

    def __init__(self):
        self._teams = {}
        self.clients_low = np.random.normal(100, 20, 100).astype(int)

    @property
    def teams(self) -> Dict[int, Team]:
        return self._teams

    def add_team(self, t: Team):
        self._teams[t.id] = t

    def get_team(self, id: int) -> Team:
        return self._teams[id]

    def get_random_clients_low(self):
        return self.clients_low
