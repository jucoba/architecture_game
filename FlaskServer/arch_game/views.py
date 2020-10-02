from flask import Flask, request
from arch_game import app
import random
from arch_game.parser.json_parser import JsonParser
from arch_game.game.game_logic import GameLogic

logic = GameLogic()


@app.route('/register_team', methods=['POST'])
def register_team():
    print(request.json)
    parser = JsonParser()
    team = parser.create_team(request.json)
    logic.register_new_team(team)
    print('There are {0} registered teams'.format(len(logic.teams)))
    return str(team.id)
