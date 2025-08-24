import sqlite3

connection = sqlite3.connect(r"august\24.08.2025\school.db")
cursor = connection.cursor()

cursor.execute('SELECT * FROM books')
d = cursor.description

for i in d:
    print(i[0], i[1], i[2])