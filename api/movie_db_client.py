import requests
import urllib.parse


class MovieDbClient:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.auth_header = {"Authorization": f"Bearer {self.api_key}"}

    def search_movies(self, query):
        encoded_query = urllib.parse.quote(query)
        url = f'{self.BASE_URL}/search/movie'

        response = requests.get(url, params={"query": encoded_query}, headers=self.auth_header)
        if response.status_code == 200:
            return response.json()

        return {}

    def get_movie_details(self, id):
        url = f'{self.BASE_URL}/movie/{id}'

        response = requests.get(url, headers=self.auth_header)
        if response.status_code == 200:
            return response.json()

        return {}
