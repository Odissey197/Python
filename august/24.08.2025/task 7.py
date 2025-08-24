import sqlite3

connection = sqlite3.connect(r"august\24.08.2025\school.db")
cursor = connection.cursor()

cursor.execute('SELECT * FROM wallets')
d = cursor.description

for i in d:
    print(i[0])

name_list = [i[0] for i in d]
print(name_list)