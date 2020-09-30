from flask import Flask, request
from arch_game import app
import random
from arch_game.parser.json_parser import JsonParser




@app.route('/register_team', methods=['GET', 'POST'])
def register_team():
    print(request.json)
    parser = JsonParser()
    print(parser.create_team(request.json))
    return str(random.randint(1000, 9999))
