from alkahest.blueprints import init_get_blueprint


def init_alkahest(app, session):
    # Add the session to the app object.
    app.session = session

    # Initialize get blueprints
    init_get_blueprint(app)
