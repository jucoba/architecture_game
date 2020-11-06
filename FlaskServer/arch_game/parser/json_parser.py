from typing import Dict
import json
from arch_game.game.team import Team


class JsonParser:

    @staticmethod
    def create_team(team_dict: Dict):
        team_name = team_dict["team_name"]
        player_name = team_dict["player_name"]
        team = Team(team_name, player_name)
        return team

    def parse_team(self, team: Team):
        team_dict = {
            "id": team.id,
            "team_name": team.team_name,
            "cicle_cost": team.cicle_cost,
            "architecture_level": team.architecture_level,
            "balance": team.balance,
            "capacity": team.capacity,
            "income": team.income,
            "pyg": team.pyg,
            "current_clients": team.current_clients,
            "leads": team.leads,
            "can_receive_new_clients": team.can_receive_new_clients,

        }
        for value in team_dict:
            print(value +":"+str(type(team_dict[value])))

        return team_dict
