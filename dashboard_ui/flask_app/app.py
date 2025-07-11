from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Absolute DB path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

USERNAME = 'tenant'
PASSWORD = 'securepass'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # ✅ Use real column names:
        cursor.execute('SELECT timestamp, tenant_id, ip_address, action FROM access_logs')
        logs = cursor.fetchall()
        conn.close()
    except Exception as e:
        return f"Database Error: {str(e)}"

    return render_template('index.html', logs=logs)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

