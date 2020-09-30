from typing import Dict, Any
from arch_game.game.team import Team


class GameBoard:
    teams: Dict[int, Team]

    def __init__(self):
        self._teams = {}

    @property
    def teams(self) -> Dict[int, Team]:
        return self._teams

    def add_team(self, t: Team):
        self._teams[t.id] = t
    
    def get_team(self, id:int) -> Team:
        return self._teams[id]
