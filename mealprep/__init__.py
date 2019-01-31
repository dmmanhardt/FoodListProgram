import os
from flask import Flask
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    # creates and configures app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    base_directory = os.path.dirname(os.path.abspath(__file__))
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(base_directory, 'mealprep.sqlite'),
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from mealprep import db
    db.init_app(app)
    
    from mealprep import create
    app.register_blueprint(create.bp)
    app.add_url_rule('/', endpoint='index')

    return app