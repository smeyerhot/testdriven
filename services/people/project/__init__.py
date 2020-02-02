# services/users/project/__init__.py


from flask import Flask, jsonify
from flask_restful import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)
app.config.from_object('project.config.DevelopmentConfig')  # new

class PeoplePing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }
class People(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'hello!'
    }


api.add_resource(PeoplePing, '/people/ping')
api.add_resource(People, '/people')