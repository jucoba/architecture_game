from typing import Dict


from src.game.team import Team


class JsonParser:

    @staticmethod
    def create_team(team_dict: Dict):
        team_name = team_dict["team_name"]
        player_name = team_dict["player_name"]
        team = Team(team_name, player_name)
        return team
