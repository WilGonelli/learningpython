'''
Docstring for books_api.api.schemas.book
'''

from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    publish_date: str
    description: str