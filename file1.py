import sqlite3
from flask import Flask, request

app = Flask(name)

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()


if name == 'main':
    app.run()
