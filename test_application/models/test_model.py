from sqlalchemy import Column, Integer, String
from alkahest.mixin import Alkahest

from test_application.models import Model


class TestModel(Model, Alkahest):
    __tablename__ = 'test_model'
    resource_name = 'woo'

    id = Column(Integer, primary_key=True)
    string_1 = Column(String)
    string_2 = Column(String)

    def ding():
        return 3
