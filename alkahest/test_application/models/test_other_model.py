from sqlalchemy import Column, Integer, String
from alkahest import AlkahestMixin

from alkahest.models import Model


class TestOtherModel(Model, AlkahestMixin):
    __tablename__ = 'test_model'

    id = Column(Integer, primary_key=True)
    integer = Column(Integer)
    string_2 = Column(String)

    def ding():
        return 3
