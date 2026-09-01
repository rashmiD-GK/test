import sqlite3
from flask import Flask, request

app = Flask(name)

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ✅ Safe: Parameterized query
    query = "SELECT  FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    result = cursor.fetchall()
    conn.close()
    return str(result)

if name == 'main':
    app.run()
