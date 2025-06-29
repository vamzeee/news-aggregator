from src.storage.models.article import Article

from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

#TODO : implement a cache
@app.route('/')
def index() :
    db_path = os.path.join('data', 'news_aggregator.db')
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM articles ORDER BY published_at DESC')
    rows = cursor.fetchall()

    articles = [Article.from_db_tuple(row) for row in rows]
    connection.close()

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)