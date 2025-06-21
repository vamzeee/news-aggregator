from abc import ABC, abstractmethod

class BaseIngestor(ABC) :

    @abstractmethod
    def fetch_articles(self, query:str, max_results:int = 10) :
        """fetches max_results articles from the given query API"""
        pass
