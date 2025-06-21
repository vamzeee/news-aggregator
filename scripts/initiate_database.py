import sqlite3
import os

db_path = os.path.join('data', 'news_aggregator.db')

connection = sqlite3.connect(db_path)

cursor = connection.cursor()

# articles table :
# id - autoincremented integer
# url - unique identifier
# title
# description
# content
# published_at
# source_name
# api_source - metadata
# ingested_at - metadata
#cursor.execute('CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT UNIQUE NOT NULL, title TEXT NOT NULL, description TEXT, content TEXT, published_at TIMESTAMP, source_name TEXT, api_source TEXT NOT NULL, ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')

# TODO : Topics table
# TODO : Articles-Topics relationship table
# TODO : logs?
# TODO : table to track topic_updates
# TODO : indexes
try:
    cursor.execute("PRAGMA table_info(articles)")
    columns = cursor.fetchall()
    print("Table Structure : ")
    for col in columns :
        print(f"  {col[1]} ({col[2]})")

except sqlite3.Error as e:
        print("Error : ", e)

connection.close()

