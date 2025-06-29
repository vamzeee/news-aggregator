from src.storage.models.article import Article
import re


def clean_content(article: Article) :
    # content field
    content = article.content
    if not content == None:
        content = content.replace('\r', '').replace('\n', '')
        content = re.sub(r'…\s*\[\+\d+\s+chars\]', '', content)
        content = content.strip()
        article.content = content

    #description field
    description = article.description
    if not description == None:
        description = re.sub(r'[,…]+\s*$', '', description)
        description = re.sub(r'\s+', ' ', description)
        description = description.replace("\\'", "'")
        description = description.strip()
        article.description = description

def parse_articles(news) -> list:
    articles = []
    for element in news['articles'] :
        article = Article.from_newsapi_response(element)
        clean_content(article)
        articles.append(article)
    return articles


