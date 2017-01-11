from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from alkahest.models import Model

from test_application.models.test_model import TestModel
from test_application.models.test_other_model import TestOtherModel

engine = create_engine(environ.get('SQLALCHEMY_DB_URL'), convert_unicode=True)
# Destroy existing db
Model.metadata.drop_all(bind=engine)
print('Destroyed existing database')
# Recreate
Model.metadata.create_all(bind=engine)
session = scoped_session(sessionmaker(autocommit=False, autoflush=True,
                                      bind=engine))

session.add(TestModel('wow', 'owo'))
session.add(TestModel('ayyy', 'lmao'))

session.add(TestOtherModel('a', '1'))
session.add(TestOtherModel('b', '123'))

session.commit()

print('Creating database complete')
