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


# topics table :
# id - autoincremented integer
# name - name of the topic
# keywords - keywords associated with the topic
# enabled - to disable topics that are not necessary
#cursor.execute('CREATE TABLE topics (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, keywords TEXT NOT NULL, enabled BOOLEAN DEFAULT 1)')


# TODO : Articles-Topics relationship table
# TODO : logs?
# TODO : table to track topic_updates
# TODO : indexes
# try:
#     cursor.execute("PRAGMA table_info(topics)")
#     columns = cursor.fetchall()
#     print("Table Structure : ")
#     for col in columns :
#         print(f"  {col[1]} ({col[2]})")

# except sqlite3.Error as e:
#         print("Error : ", e)

# !!!!! CAREFUL !!!!!!
# ------------------------ delete articles
# cursor.execute('DELETE from articles')


# ------------------------ check size of articles table
#cursor.execute('SELECT COUNT(*) FROM articles')

# ------------------------ check size of topics table
#cursor.execute('SELECT COUNT(*) FROM topics')

#print(cursor.fetchone()[0])
#connection.commit()

connection.close()

