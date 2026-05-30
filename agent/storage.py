import sqlite3
from typing import List, Tuple


class SQLiteStorage:
    def __init__(self, db_path: str = "agent.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    response TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()

    def save_conversation(self, task: str, response: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO conversations (task, response) VALUES (?, ?)",
                (task, response),
            )
            conn.commit()

    def list_conversations(self, limit: int = 50) -> List[Tuple[int, str, str, str]]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, task, response, created_at FROM conversations ORDER BY id DESC LIMIT ?",
                (limit,),
            )
            return cur.fetchall()
