from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    movie_db_id = db.Column(db.Integer)
    director = db.Column(db.String())
    image_path = db.Column(db.String())
    released = db.Column(db.Date())
    added = db.Column(db.Date())
    watched = db.Column(db.Date())
    imdb_id = db.Column(db.Integer())
    rotten_tomatoes_id = db.Column(db.Integer())

    def __init__(self, name: str, movie_db_id: int):
        self.name = name
        self.movie_db_id = movie_db_id
        self.added = date.today()
