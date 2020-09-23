from flask import Flask
from flask import render_template

import random



app = Flask(__name__, static_url_path='/')

@app.route("/app")
def home():
    return app.send_static_file('index.html')

@app.route('/register_team')
def register_team():
    return str(random.randint(1000,9999))