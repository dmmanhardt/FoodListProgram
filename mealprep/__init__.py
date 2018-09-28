import os
from flask import Flask


def create_app(test_config=None):
    # creates and configures app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    from . import create
    app.register_blueprint(create.bp)
    app.add_url_rule('/', endpoint='index')

    return app