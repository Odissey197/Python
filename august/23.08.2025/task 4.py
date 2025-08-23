import sqlite3

connection = sqlite3.connect(r"august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute('''
CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    age INTEGER,
    profession VARCHAR(50) NOT NULL
)
''')

connection.commit()