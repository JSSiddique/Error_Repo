# vulnerable_app.py

import sqlite3
from flask import Flask, request

app = Flask(__name__)

# ❌ Hardcoded secret (security issue)
SECRET_KEY = "mysecret123"


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    # ❌ No proper authentication handling
    if user:
        return "Login successful"
    else:
        return "Login failed"


@app.route('/read_file')
def read_file():
    filename = request.args.get("file")

    # ❌ Path Traversal vulnerability
    with open(filename, "r") as f:
        return f.read()


def divide(a, b):
    # ❌ No error handling (ZeroDivision)
    return a / b


def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ No input validation
    cursor.execute("SELECT * FROM users WHERE id=" + user_id)

    return cursor.fetchone()


if __name__ == "__main__":
    # ❌ Debug mode ON (security risk)
    app.run(debug=True)