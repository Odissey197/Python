import sqlite3

connection = sqlite3.connect(r"august\24.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM workers")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()