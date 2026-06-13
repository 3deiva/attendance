
import sqlite3
import pickle

DB_NAME = "attendance.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        encoding BLOB
    )
    ''')
CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        encoding BLOB
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

def add_user(username, encoding):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, encoding) VALUES (?, ?)",
        (username, pickle.dumps(encoding))
    )

    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT username, encoding FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row:
        import pickle
        return {
            "username": row[0],
            "encoding": pickle.loads(row[1])
        }
    return None
