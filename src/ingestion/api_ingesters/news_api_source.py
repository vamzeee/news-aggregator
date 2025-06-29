from src.ingestion.api_ingesters.base_source import BaseIngestor

from dotenv import dotenv_values
import requests

class NewsAPIIngestor(BaseIngestor) :
    def __init__(self):
        config = dotenv_values('.env')

        self.api_key = config['NEWS_API_KEY']
        self.endpoint = 'https://newsapi.org/v2/top-headlines'
    
    def fetch_articles(self, category, max_results = 50):
        params = {
            'category' : category,
            'pageSize' : max_results,
            'apiKey' : self.api_key
        }

        response = requests.get(self.endpoint, params=params)

        if response.status_code == 200 :
            return response.json()
        else :
            print('Request failed with status code : ', response.status_code)
            return ''
            