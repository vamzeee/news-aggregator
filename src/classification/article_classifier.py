from src.classification.article_document_creator import retrieve_all_articles
from src.classification.topic_document_creator import retrieve_all_topics
from src.classification.t
def classify_articles() :
    
    articles = retrieve_all_articles()

    topics = retrieve_all_topics()

    vocabulary = 
