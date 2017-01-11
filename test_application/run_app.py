from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import alkahest

from flask import Flask

from test_application.models import Model

from test_application.models.test_model import TestModel
from test_application.models.test_other_model import TestOtherModel


def setup_database(app, session):
    Model.metadata.drop_all(bind=app.engine)
    print('Destroyed existing database')
    # Recreate
    Model.metadata.create_all(bind=app.engine)

    session.add(TestModel(string_1='wow', string_2='owo'))
    session.add(TestModel(string_1='ayyy', string_2='lmao'))

    session.add(TestOtherModel(string_1='a', integer_1=13))
    session.add(TestOtherModel(string_1='b', integer_1=55))

    session.commit()


def create_engine_and_session(app):
    """ Initialize the database session on the given app. """
    app.engine = create_engine('sqlite:////tmp/alkahest.db',
                               convert_unicode=True)

    return create_session(app.engine)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        app.session.remove()


def create_session(engine):
    return scoped_session(sessionmaker(autocommit=False,
                                       autoflush=True,
                                       bind=engine))


def create_app():
    """ Create and return instance of :class:`flask.Flask`.

    :return: Instance of :class:`flask.Flask`.
    """
    app = Flask(__name__)

    session = create_engine_and_session(app)

    setup_database(app, session)
    alkahest.init_alkahest(app, session)
    return app


if __name__ == '__main__':
    create_app().run(debug=True, host="0.0.0.0")
