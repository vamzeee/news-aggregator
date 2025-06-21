import sqlite3
from datetime import datetime
import os

def check_size() :
    db_path = os.path.join('data', 'news_aggregator.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM articles")
    total_count = cursor.fetchone()[0]

    print('Number of articles present : ', total_count)
    connection.close()

check_size()