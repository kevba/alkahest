from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from alkahest.mixin import Alkahest

from test_application.models import Model


class Book(Model, Alkahest):
    __tablename__ = 'book'
    resource_name = 'books'

    id = Column(Integer, primary_key=True)
    isbn = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    library_id = Column(Integer, ForeignKey('library.id'))
    library = relationship('Library')
