import sqlite3

connection = sqlite3.connect(r"august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")