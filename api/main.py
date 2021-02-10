from flask import Flask, request
from models import db, Film
import os
from movie_db_client import MovieDbClient

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("TRACKER_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

movie_db_client = MovieDbClient(os.environ.get("MOVIE_DB_API_KEY"))

@app.route('/')
def hello_world():
    return 'TODO: List routes'


@app.route('/films', methods=['GET'])
def get_films():
    """Get a paginated list of all films"""

    # TODO: Get films from DB

    return {
        "count": 10,
        "max": 100,
        "films": {
            "id": 1,
            "name": "Marriage Story",
            "director": "",
            "movie_db_id": 492188,
            "image_path": "blah.png",
            "released": "2019-11-06",
            "genres": ["drama"],
            "imdb": {
                "link": "https://www.imdb.com/title/tt7653254/",
                "score": 7.9
            },
            "rotten_tomatoes": {
                "link": "https://www.rottentomatoes.com/m/marriage_story_2019",
                "score": 94
            },
            "watched": None
        }
    }


@app.route('/films', methods=['POST'])
def add_film():
    """
    Add a new film to the collection

    Request schema:
    {
      "name": string,
      "movie_db_id": integer
    }
    """

    # TODO: Add film to DB

    content = request.json

    # TODO: populate model with details results
    # TODO: Download poster image
    # TODO: Find director
    # TODO: Find rotten tomatoes ID
    movie_details = movie_db_client.get_movie_details(content["movie_db_id"])

    new_film = Film(content["name"], content["movie_db_id"])
    new_film.released = movie_details["release_date"]
    new_film.imdb_id = movie_details["imdb_id"]

    db.session.add(new_film)
    db.session.commit()

    return {
        "id": new_film.id,
        "name": new_film.name,
        "movie_db_id": new_film.movie_db_id,
        "released": new_film.released,
        "imdb_id": new_film.imdb_id
    }


if __name__ == '__main__':
    app.run(debug=True)
