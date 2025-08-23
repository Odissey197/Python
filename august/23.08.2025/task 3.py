import sqlite3

connection = sqlite3.connect(r"august\23.08.2025\school.db")
cursor = connection.cursor()
print("База данных успешно подключена!")

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

print(columns)
data = [dict(zip(columns, row)) for row in rows]

#print(rows)

for row in rows:
    print(row)

cursor.close()