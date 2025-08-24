import sqlite3

connection = sqlite3.connect(r"august\24.08.2025\school.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IS NOT EXISTS wallets (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        teacher_id INTEGER NOT NULL,
        balance INTEGER NOT NULL CHECK(balance >= 0),
        is_active INTEGER DEFAULT I CHECK(is_active IN (0, 1)),
        FOREIGN KEY (teacher_id) REFERENCES teachers (id))
""")