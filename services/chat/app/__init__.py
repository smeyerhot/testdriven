from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send
from flask_cors import CORS  

# instantiate the extensions
socketio = SocketIO()
cors = CORS()  

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    socketio.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # shell context for flask cli
    app.shell_context_processor({"app": app})

    return app

