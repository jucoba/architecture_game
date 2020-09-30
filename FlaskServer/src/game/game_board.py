from typing import Dict, Any
from src.game.team import Team


class GameBoard:
    teams: Dict[int, Team]

    def __init__(self):
        self._teams = {}

    @property
    def teams(self):
        return self._teams

    def add_team(self, t: Team):
        self._teams[t.id] = t
