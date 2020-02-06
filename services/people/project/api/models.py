# services/people/project/api/views.py
from sqlalchemy.sql import func

from project import db



class Movie(db.Model):

    __tablename__ = 'people'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating