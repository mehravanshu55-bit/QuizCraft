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
