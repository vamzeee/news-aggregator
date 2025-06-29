from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Article:
    url: str
    title: str
    api_source: str
    description: Optional[str] = None
    content: Optional[str] = None
    published_at: Optional[datetime] = None
    source_name: Optional[str] = None
    ingested_at: Optional[datetime] = None
    id: Optional[int] = None

    @classmethod
    def from_newsapi_response(cls, article_data: dict, api_source: str = "newsapi"):
        """Create Article from NewsAPI response"""
        return cls(
            url=article_data.get('url'),
            title=article_data.get('title'),
            description=article_data.get('description'),
            content=article_data.get('content'),
            published_at=article_data.get('publishedAt'),
            source_name=article_data.get('source', {}).get('name'),
            api_source=api_source
        )
    
    def to_db_tuple(self):
        """Convert to a tuple for SQL insertion"""
        return (self.url, self.title, self.description, self.content, self.published_at, self.source_name, self.api_source)
    
    @classmethod
    def from_db_tuple(cls, row):
        """Create Article from database row"""
        return cls(
            id = row['id'],
            url = row['url'],
            title = row['title'],
            api_source = row['api_source'],
            description = row['description'],
            content = row['content'],
            published_at = row['published_at'],
            source_name = row['source_name'],
            ingested_at = row['ingested_at']
        )