import sqlite3
import os

def insert_articles_batch(articles: list) :
    db_path = os.path.join('data', 'news_aggregator.db')
    connection = sqlite3.connect(db_path)

    cursor = connection.cursor()

    success_count = 0
    failure_count = 0

    for article in articles :
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO articles 
                (url, title, description, content, published_at, source_name, api_source)
                VALUES (?, ?, ?, ?, ?, ?, ?)""", article.to_db_tuple())
            success_count+=1
        except Exception as e :
            print(f"Failed to insert {article.url}: {e}")
            failure_count += 1
    
    connection.commit()
    connection.close()

    return success_count, failure_count
