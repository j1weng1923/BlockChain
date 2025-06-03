from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Cho phép frontend gọi API từ domain khác

DB_NAME = 'winners.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS winners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            round INTEGER NOT NULL,
            winner_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/winners', methods=['GET'])
def get_winners():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT round, winner_name FROM winners ORDER BY round ASC')
    rows = c.fetchall()
    conn.close()
    return jsonify([{'round': r[0], 'winner': r[1]} for r in rows])

@app.route('/winners', methods=['POST'])
def add_winner():
    data = request.get_json()
    round_num = data.get('round')
    winner_name = data.get('winner')

    if round_num is None or not winner_name:
        return jsonify({'error': 'Missing round or winner'}), 400

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO winners (round, winner_name) VALUES (?, ?)', (round_num, winner_name))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Winner added'}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

