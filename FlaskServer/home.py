from flask import Flask
import random

app = Flask(__name__)

@app.route('/register_team')
def register_team():
    return str(random.randint(1000,9999))