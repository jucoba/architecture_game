import json

from src.game.team import Team



class JsonParser:

    @staticmethod
    def create_team(json_str: str):
        json_team = json.loads(json_str)
        team_name = json_team["team_name"]
        player_name = json_team["player_name"]
        team = Team(team_name, player_name)
        return team
