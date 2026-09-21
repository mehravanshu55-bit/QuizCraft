import sqlite3

def init_db():
    conn = sqlite3.connect("quizcraft.db")
    cursor = conn.cursor()

    cursor.execute("""
         CREATE TABLE IF NOT EXISTS users (
         id INTEGER PRIMARY KEY, 
         name TEXT NOT NULL,
         username TEXT UNIQUE NOT NULL,
         password TEXT NOT NULL
    )
""")
    conn.commit()
    conn.close()

def create_user(name,username,password): 
    conn = sqlite3.connect("quizcraft.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (name, username, password) VALUES(?, ?, ?)",
                       (name, username, password)
        )
        conn.commit()
        return True
    
    except sqlite3.IntegrityError:
        return False
    
    finally:
        conn.close()

def check_user(username, password):
    conn = sqlite3.connect("quizcraft.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()
    return user
