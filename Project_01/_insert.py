import sqlite3

conn = sqlite3.connect('digimons.db')

nome_digimon = 'Agumon'

conn.execute("INSERT INTO digimons (nome) VALUES ('{}')".format(nome_digimon))

conn.commit()

conn.close()
