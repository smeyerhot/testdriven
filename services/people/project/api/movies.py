# services/people/project/api/views.py
from flask import Blueprint,jsonify,request
from project import db
from flask_restful import Resource, Api
from .models import Movie



people_blueprint = Blueprint('people', __name__)

api = Api(people_blueprint)


# class Movies(Resource):
#     def get(self):
#         # """Get single user details"""
#         # movies_list = Movie.query.all()
#         # movies = []
#         # for movie in movies_list:
#         #     movies.append({'title': movie.title, 'rating': movie.rating})
        
#         # return jsonify({'movies': movies})
        
class MoviesList(Resource):
    def post(self):
        post_data = request.get_json(force=True)
        title = post_data.get('title')
        rating = post_data.get('rating')
        db.session.add(Movie(title=title,rating=rating))
        db.session.commit()
        
        return jsonify({'status': 'success',
            'message': f'{title} was added!'})
        


    def get(self):
        movies_list = Movie.query.all()
        movies = []
        for movie in movies_list:
            movies.append({'title': movie.title, 'rating': movie.rating})

        return jsonify({'movies': movies})

class PeoplePing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

# @people_blueprint.route('/add_movie', methods=['POST'])
# def add_movie():
#     movie_data = request.get_json(force=True)
#     new_movie = Movie(title=movie_data['title'],rating=movie_data['rating'])
#     db.session.add(new_movie)
#     db.session.commit()


#     return 'Done', 201

# @people_blueprint.route('/',methods=['POST','GET'])
# def movies():
#     movies_list = Movie.query.all()
#     movies = []
#     for movie in movies_list:
#         movies.append({'title': movie.title, 'rating': movie.rating})
#     return jsonify({'movies': movies})

api.add_resource(PeoplePing, '/people/ping')

api.add_resource(MoviesList, '/people')
# api.add_resource(Movies, '/people')