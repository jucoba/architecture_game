import unittest
from arch_game.parser.json_parser import JsonParser
from arch_game.game.team import Team


class TestJsonPareser(unittest.TestCase):

    def test_convert_new_team_json_to_team(self):
        parser = JsonParser()
        team_dictionary = {'team_name': 'a', 'player_name': 'b'}
        team: Team = parser.create_team(team_dictionary)
        self.assertEqual(team.team_name, "a")

    def test_team_jsonify(self):
        parser = JsonParser()
        t = Team("A team", "Mario")
        json_t = parser.parse_team(t)
        self.assertEqual(json_t["id"], t.id)
        self.assertEqual(json_t["team_name"], t.team_name)
        self.assertEqual(json_t["cicle_cost"], t.cicle_cost)
        self.assertEqual(json_t["architecture_level"], t.architecture_level)
        self.assertEqual(json_t["balance"], t.balance)
        self.assertEqual(json_t["capacity"], t.capacity)
        self.assertEqual(json_t["income"], t.income)
        self.assertEqual(json_t["pyg"], t.pyg)
        self.assertEqual(json_t["current_clients"], t.current_clients)
        self.assertEqual(json_t["can_receive_new_clients"], t.can_receive_new_clients)

    def test_update_team(self):
        parser = JsonParser()
        team_dictionary = {
            'team_name': 'a',
            'player_name': 'b'

        }

