import requests
from app import app
from models import Song


ECHO_NEST_KEY = app.config['ECHO_NEST_KEY']


def search_for_artist(artist):
    """
    Search echo nest api to retrieve id for artist
    """
    search_endpoint = 'http://developer.echonest.com/api/v4/artist/search'
    search_params = {
        'api_key': ECHO_NEST_KEY,
        'format': 'json',
        'results': 1,
        'name': artist
    }
    r = requests.get(search_endpoint, params=search_params)
    search_json = r.json()
    artist_id = search_json['response']['artists'][0]['id']
    return artist_id


def get_artist_genres(artist):
    """
    Return the top genres for an artist
    :param artist: the name of the artist
    :return: an array of the artist's genres
    """
    profile_endpoint = 'http://developer.echonest.com/api/v4/artist/profile'
    profile_params = {
        'api_key': ECHO_NEST_KEY,
        'name': artist,
        'format': 'json',
        'bucket': 'genre'
    }
    r = requests.get(profile_endpoint, params=profile_params)
    genre_json = r.json()
    genre_dict = genre_json['response']['artist']['genres']
    return [genre['name'] for genre in genre_dict]
