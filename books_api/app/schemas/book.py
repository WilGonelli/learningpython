'''
Docstring for books_api.api.schemas.book
'''

from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    title: str
    autor: str
    publish_date: datetime
    description: str