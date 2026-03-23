import sqlite3

def create_connection(path: str) -> sqlite3.Connection:
    return sqlite3.connect(path)
