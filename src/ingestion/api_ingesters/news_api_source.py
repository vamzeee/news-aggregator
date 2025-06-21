from src.ingestion.api_ingesters.base_source import BaseIngestor

from dotenv import dotenv_values
import requests

class NewsAPIIngestor(BaseIngestor) :
    def __init__(self):
        config = dotenv_values('.env')

        self.api_key = config['NEWS_API_KEY']
        self.endpoint = 'https://newsapi.org/v2/everything'
    
    def fetch_articles(self, query, max_results = 10):
        params = {
            'q' : query,
            'pageSize' : max_results,
            'apiKey' : self.api_key
        }

        response = requests.get(self.endpoint, params=params)

        if response.status_code == 200 :
            return response.json()
        else :
            print('Request failed with status code : ', response.status_code)
            return ''
            