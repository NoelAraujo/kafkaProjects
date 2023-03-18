import sqlite3  

conn = sqlite3.connect('digimons.db')  

conn.execute('''CREATE TABLE digimons (id INTEGER PRIMARY KEY, nome TEXT NOT NULL);''')  

conn.close()  

 