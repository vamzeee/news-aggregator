from src.storage.models.topic import Topic

import sqlite3
import os

def retrieve_all_topics() -> list :
    connection = sqlite3.connect(os.path.join('data', 'news_aggregator.db'))
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM topics ORDER BY published_at DESC')
    rows = cursor.fetchall() 

    topics = [Topic.from_db_tuple(row) for row in rows]

    return topics