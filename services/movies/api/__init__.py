
from flask import Flask, jsonify, Response
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

# instantiate the app
# app = Flask(__name__) #These will break app if instantiated too early
db = SQLAlchemy()
cors = CORS()
# api = Api(app)
# app.config.from_object('project.config.DevelopmentConfig')  # new
# app_settings = os.en


def create_app():
    app = Flask(__name__)
    
    # app_settings = os.getenv('APP_SETTINGS')
    # app.config.from_object(app_settings)

    # api = Api(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    return app