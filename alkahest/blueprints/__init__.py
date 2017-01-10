from alkahest.blueprints.get_blueprint import bp as get


def init_get_blueprint(app, prefix='/api'):
    app.register_blueprint(get, url_prefix=prefix)
