from sqlalchemy import Column, Integer, String
from alkahest.mixin import Alkahest

from test_application.models import Model


class TestOtherModel(Model, Alkahest):
    __tablename__ = 'test_other_model'

    id = Column(Integer, primary_key=True)
    integer_1 = Column(Integer)
    string_1 = Column(String)

    def ding():
        return 3
