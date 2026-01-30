import psycopg2
from flask import g

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host="db",
            database="code_library",
            user="user",
            password="password"
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()