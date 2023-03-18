import sqlite3

# Connect to the database
conn = sqlite3.connect('digimons.db')

# Create a cursor object
c = conn.cursor()

# Execute the DELETE statement to remove all data from the table
c.execute('DELETE FROM digimons')

# Commit the changes and close the connection
conn.commit()
conn.close()
