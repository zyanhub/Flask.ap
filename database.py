import sqlite3


def connect(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(path):
    with connect(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def add_entry(path, name, message):
    with connect(path) as conn:
        conn.execute(
            "INSERT INTO entries (name, message) VALUES (?, ?)", (name, message)
        )


def get_entries(path):
    with connect(path) as conn:
        return conn.execute(
            "SELECT name, message, created_at FROM entries ORDER BY id DESC"
        ).fetchall()
