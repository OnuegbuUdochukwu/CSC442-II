import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'calculations.db')

def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        image_path TEXT,
        measured_mm REAL NOT NULL,
        real_mm REAL NOT NULL,
        unit TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def insert_record(username, image_path, measured_mm, real_mm, unit):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO calculations (username, image_path, measured_mm, real_mm, unit, timestamp) VALUES (?, ?, ?, ?, ?, ?)',
                (username, image_path, measured_mm, real_mm, unit, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def list_records():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, username, image_path, measured_mm, real_mm, unit, timestamp FROM calculations ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_record(record_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM calculations WHERE id=?', (record_id,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
