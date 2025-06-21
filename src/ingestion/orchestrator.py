from src.ingestion.api_ingesters.news_api_source import NewsAPIIngestor
from src.ingestion.content_cleaners.newsapi_cleaner import parse_articles
from src.ingestion.article_inserter import insert_articles_batch
from src.storage.models.article import Article

def fetch_news(query:str) :
    # ingest from API
    ingestor = NewsAPIIngestor()
    news = ingestor.fetch_articles(query)

    if not news == '' :
        # parse and clean the response
        articles = parse_articles(news)
        success,failures = insert_articles_batch(articles)
        print('Managed to commit {0} articles'.format(success))
        print('Failed to commit {0} articles'.format(failures))