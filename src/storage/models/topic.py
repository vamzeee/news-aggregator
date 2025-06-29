from dataclasses import dataclass
from typing import Optional

@dataclass
class Topic:
    id: Optional[int] = None
    name: str
    keywords: str
    enabled: bool

    @classmethod
    def from_db_tuple(cls, row):
        """Create Topic from database row"""
        return cls(
            id = row['id'],
            name = row['name']
            keywords = row['keywords']
            enabled = row['enabled']
        )