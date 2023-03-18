from kafka import KafkaConsumer
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('digimons.db')
c = conn.cursor()


# Create a Kafka consumer for the topic
consumer = KafkaConsumer('digimons',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest')

# Consume messages from the topic and insert them into the database
for message in consumer:
    value = message.value.decode('utf-8')
    print(value)
    c.execute("INSERT INTO digimons (nome) VALUES (?)", (value,))
    conn.commit()
    print('inserido')

# Close the database connection
conn.close()
