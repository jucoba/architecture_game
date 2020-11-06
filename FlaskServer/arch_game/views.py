from flask import Flask, request
from arch_game import app
import random
from arch_game.parser.json_parser import JsonParser
from arch_game.game.game_logic import GameLogic
from flask import abort, jsonify

logic = GameLogic()


@app.route('/register_team', methods=['POST'])
def register_team():
    print(request.json)
    parser = JsonParser()
    team = parser.create_team(request.json)
    logic.register_new_team(team)
    print('There are {0} registered teams'.format(len(logic.teams)))
    return jsonify({'id': team.id})


@app.route('/team/<int:id>', methods=['GET'])
def get_team(id):
    team_list = logic.teams
    if id not in team_list:
        abort(404, description="Team not found")
    else:
        t = team_list[id]
        parser = JsonParser()
        json_t = jsonify(parser.parse_team(t))
        print(json_t)
        return json_t


@app.route('/team/new_cicle/<int:id>', methods=['GET'])
def new_team_cicle(id):
    team_list = logic.teams
    if id not in team_list:
        abort(404, description="Team not found")
    else:
        logic.new_team_cicle(id)
        return "ok"
