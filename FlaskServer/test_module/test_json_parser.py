import unittest
from src.parser.json_parser import JsonParser
from src.game.team import Team


class TestJsonPareser(unittest.TestCase):

    def test_convert_new_team_json_to_team(self):
        parser = JsonParser()
        team_dictionary = {'team_name': 'a', 'player_name': 'b'}
        team: Team = parser.create_team(team_dictionary)
        self.assertEqual(team.team_name, "a")
