from sqlalchemy import Column, Integer, String
from alkahest import AlkahestMixin

from alkahest.models import Model


class TestModel(Model, AlkahestMixin):
    __tablename__ = 'test_model'

    id = Column(Integer, primary_key=True)
    string_1 = Column(String)
    string_2 = Column(String)

    def ding():
        return 3
