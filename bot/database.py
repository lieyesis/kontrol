import sqlite3

DB_PATH = "db.sqlite3"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS complaints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT NOT NULL,
                complaint TEXT NOT NULL
            )
        """)
        conn.commit()

def save_complaint(name, contact, complaint):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO complaints (name, contact, complaint)
            VALUES (?, ?, ?)
        """, (name, contact, complaint))
        conn.commit()
