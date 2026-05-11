import os
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import sqlite3
from datetime import datetime

BASE = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE, 'uploads')
DB_PATH = os.path.join(BASE, 'calculations_web.db')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'dev-key'

MICROSCOPE_CHOICES = [
    ('Light Microscope (40x)', 40.0),
    ('Compound Microscope (100x)', 100.0),
    ('Electron Microscope (1000x)', 1000.0),
    ('Scanning EM (20000x)', 20000.0)
]
UNIT_CONVERSIONS = {'nm':1e6,'um':1e3,'mm':1.0,'cm':0.1,'m':0.001}

def init_db():
    conn = sqlite3.connect(DB_PATH)
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
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('INSERT INTO calculations (username, image_path, measured_mm, real_mm, unit, timestamp) VALUES (?, ?, ?, ?, ?, ?)',
                (username, image_path, measured_mm, real_mm, unit, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def list_records():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT id, username, image_path, measured_mm, real_mm, unit, timestamp FROM calculations ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_record(record_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('DELETE FROM calculations WHERE id=?', (record_id,))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        measured = request.form.get('measured')
        mscope = request.form.get('mscope')
        unit = request.form.get('unit')
        if not username or not measured:
            flash('Username and measured value required')
            return redirect(url_for('index'))
        try:
            measured_mm = float(measured)
        except Exception:
            flash('Measured must be a number')
            return redirect(url_for('index'))
        mag = float(mscope)
        real_mm = measured_mm / mag

        f = request.files.get('image')
        path = None
        if f and f.filename:
            fn = secure_filename(f.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], fn)
            f.save(path)

        insert_record(username, path, measured_mm, real_mm, unit)
        flash('Calculation saved')
        return redirect(url_for('index'))
    return render_template('index.html', microscopes=MICROSCOPE_CHOICES)

@app.route('/history')
def history():
    rows = list_records()
    return render_template('history.html', rows=rows)

@app.route('/delete/<int:rec_id>')
def delete(rec_id):
    delete_record(rec_id)
    flash('Deleted')
    return redirect(url_for('history'))

@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
