from flask import Flask, request
from src.parser.json_parser import JsonPareser

import random
import sys

app = Flask(__name__, static_url_path='/')


@app.route("/app")
def home():
    return app.send_static_file('index.html')


@app.route('/register_team', methods=['GET', 'POST'])
def register_team():
    print(request.json)
    print(sys.path)
    return str(random.randint(1000, 9999))
