from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    state = random.randint(1,6)
    return jsonify({'roll':state, 'msg': f"Coucou {str(state)}"}) 