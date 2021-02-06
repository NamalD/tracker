from flask import Flask, request

app = Flask(__name__)


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

    Response schema:

    201 Created
    {
      "id": integer,
      "name": string,
      "movie_db_id": integer
    }

    303 See Other
    {
      "id": integer,
      "name": string,
      "movie_db_id": integer
    }
    """

    # TODO: Fetch data from themoviedb
    # TODO: Add film to DB

    content = request.json
    print(content)

    return {
        "id": 123,
        "name": content['name'],
        "movieDbId": content['movie_db_id'],
    }
