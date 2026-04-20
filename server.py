from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/search")
def search_user():
    # SOURCE: Entrada externa controlada por el usuario
    username = request.args.get('username')

    db = sqlite3.connect("users.db")
    cursor = db.cursor()

    # SINK: Ejecución de query con parámetro seguro
    # FIX: Evitar SQL Injection usando consulta parametrizada
    query = "SELECT * FROM profiles WHERE user = ?"
    cursor.execute(query, (username,))

    return str(cursor.fetchone())
