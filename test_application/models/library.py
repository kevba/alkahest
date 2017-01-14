from sqlalchemy import Column, Integer, String
from alkahest.mixin import Alkahest

from test_application.models import Model


class Library(Model, Alkahest):
    __tablename__ = 'library'

    id = Column(Integer, primary_key=True)
    name = Column(String)
