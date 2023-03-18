import sqlite3

conn = sqlite3.connect('digimons.db')

cursor = conn.execute("SELECT nome FROM digimons")

for row in cursor:
    print(row[0])

conn.close()
