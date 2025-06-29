from src.storage.models.article import Article
from src.classification.document_preprocessor import preprocess_document

import sqlite3
import os

def retrieve_all_articles() -> list :
    documents = []

    connection = sqlite3.connect(os.path.join('data', 'news_aggregator.db'))
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM articles ORDER BY published_at DESC')
    rows = cursor.fetchall()

    articles = [Article.from_db_tuple(row) for row in rows]
    connection.close()

    print(f'Retrieved {len(articles)} articles from db......')

    for article in articles :
        document = preprocess_document(' '.join(article.title, article.description, article.content))
        documents.append(document)
    
    return documents
