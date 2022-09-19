from flask import Flask
from flask import abort
from flask import request, jsonify

from .utilities import tic_tac_toe_winner

app = Flask(__name__)


@app.route('/winner', methods=['GET'])
def winner():
    board = request.args.get('board', '').replace('_', ' ')
    try:
        return jsonify({
            'winner': tic_tac_toe_winner(board)
        })
    except ValueError:
        abort(400)


@app.route('/winner', methods=['GET'])
def winner():
    if not request.args.get('board'):
        abort(400)
    return jsonify({'winner': None})