
import sqlite3

DB_NAME = "attendance.db"

def mark_attendance(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance (username) VALUES (?)",
        (username,)
    )

    conn.commit()
    conn.close()
