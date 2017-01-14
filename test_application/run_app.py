from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import alkahest

from flask import Flask

from test_application.models import Model

from test_application.models.book import Book
from test_application.models.library import Library


def setup_database(app, session):
    Model.metadata.create_all(bind=app.engine)
    print('created database')

    library = Library(name='My shelf')
    session.add(library)

    books = [
        Book(isbn=9783492285834, title='guards, guards!',
             author='Terry Pratchett', library=library),
        Book(isbn=9780575066564, title='Reaper man',
             author='Terry Pratchett', library=library),
        Book(isbn=978006222569, title='Equal rites',
             author='Terry Pratchett', library=library)
    ]
    session.add_all(books)

    session.commit()
    print('populated the database')


def create_engine_and_session(app):
    """ Initialize the database session on the given app. """
    app.engine = create_engine('sqlite:////tmp/alkahest.db')

    return create_session(app.engine)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        app.session.remove()


def create_session(engine):
    return scoped_session(sessionmaker(autocommit=False,
                                       autoflush=True,
                                       bind=engine))


def create_app():
    app = Flask(__name__)

    session = create_engine_and_session(app)

    setup_database(app, session)
    alkahest.init_alkahest(app, session)
    return app


if __name__ == '__main__':
    create_app().run(debug=True, host="0.0.0.0")
