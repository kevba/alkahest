from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import alkahest

from flask import Flask


def create_engine_and_session(app):
    """ Initialize the database session on the given app. """
    app.engine = create_engine(app.config['SQLALCHEMY_DB_URL'],
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

    alkahest.init_alkahest(app, session)

    return app


if __name__ == '__main__':
    create_app().run(debug=True, host="0.0.0.0")
