from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('energy.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS energy (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        voltage REAL,
                        current REAL,
                        power REAL,
                        timestamp TEXT
                    )''')
    conn.commit()
    conn.close()

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    voltage = data.get('voltage')
    current = data.get('current')
    power = voltage * current if voltage and current else None

    conn = sqlite3.connect('energy.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO energy (voltage, current, power, timestamp) VALUES (?, ?, ?, ?)",
                   (voltage, current, power, datetime.now().isoformat()))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "power": power})

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('energy.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM energy ORDER BY id DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
