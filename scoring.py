
import sqlite3


def connect_db():
    conn = sqlite3.connect("quizcraft.db")
    return conn


def create_users_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def create_history_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            topic TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            total_questions INTEGER NOT NULL,
            score INTEGER NOT NULL,
            percentage REAL NOT NULL,
            quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_user(name, username, email, password):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users
            (name, username, email, password)
            VALUES (?, ?, ?, ?)
        """, (name, username, email, password))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def check_login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    return user


def save_quiz_history(
    username,
    topic,
    difficulty,
    total_questions,
    score,
    percentage
):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO quiz_history
        (
            username,
            topic,
            difficulty,
            total_questions,
            score,
            percentage
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        username,
        topic,
        difficulty,
        total_questions,
        score,
        percentage
    ))

    conn.commit()
    conn.close()


def get_quiz_history(username):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            topic,
            difficulty,
            total_questions,
            score,
            percentage,
            quiz_date
        FROM quiz_history
        WHERE username = ?
        ORDER BY id DESC
    """, (username,))

    history = cursor.fetchall()

    conn.close()

    return history
