import sqlite3


def connect_db():
    conn = sqlite3.connect("quizcraft.db")
    return conn
