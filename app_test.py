from dotenv import load_dotenv
load_dotenv()
import os

bearer_token = os.environ['BEARER_TOKEN']

from app import app

header = {"Authorization": "Bearer "+ bearer_token}

def test_hello():
    """
    Test function to check home endpoint
    """
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_create_user():
    """
    Test function to test /create_user endpoint
    """
    response = app.test_client(
        ).get('/create_user', json={"user_name": "Vishal"})
    assert response.status_code == 200


def test_create_user_wrong_input():
    """
    Test function to test /create_user with absent params
    """
    response = app.test_client().get('/create_user', json={})
    assert response.status_code == 422


def test_search_move():
    """
    Test function to test /search_movie endpoint
    """
    response = app.test_client(
        ).get('/search_movie', json={"movie_name": "The Wizard of Oz"}, headers=header)
    assert response.status_code == 200


def test_search_move_wrong_input():
    """
    Test function to test /search_movie with absent params
    """
    response = app.test_client().get('/search_movie', json={}, headers=header)
    assert response.status_code == 422

def test_search_move_without_authentication():
    """
    Test function to test /search_movie without authentication header
    """
    response = app.test_client(
        ).get('/search_movie', json={"movie_name": "The Wizard of Oz"})
    assert response.status_code == 401


def test_update_movie_wrong_input():
    """
    Test function to test /update_movie endpoint without params
    """
    response = app.test_client().put('/update_movie', json={}, headers=header)
    assert response.status_code == 422


def test_update_movie():
    """
    Test function to test /update_movie endpoint
    """
    response = app.test_client().put('/update_movie', json={"movie_name": "The Wizard of Oz", "movie_data": {
                                                            "99popularity": 53.0,
                                                            "director": "Larry Semon",
                                                            "genre": [
                                                            "Comedy",
                                                            " Family",
                                                            " Fantasy",
                                                            " Adventure"
                                                            ],
                                                            "imdb_score": 5.3,
                                                            "name": "The Wizard of Oz"
                                                            }}, headers=header)
    assert response.status_code == 200

def test_update_movie_without_authorization():
    """
    Test function to test /update_movie without authorization
    """
    response = app.test_client().put('/update_movie', json={"movie_name": "The Wizard of Oz", "movie_data": {
                                                            "99popularity": 53.0,
                                                            "director": "Larry Semon",
                                                            "genre": [
                                                            "Comedy",
                                                            " Family",
                                                            " Fantasy",
                                                            " Adventure"
                                                            ],
                                                            "imdb_score": 5.3,
                                                            "name": "The Wizard of Oz"
                                                            }})
    assert response.status_code == 401

def test_update_movie_wrong_method():
    """
    Test function to test /update_movie with wrong request method
    """
    response = app.test_client().get('/update_movie', json={"movie_name": "The Wizard of Oz", "movie_data": {
                                                            "99popularity": 53.0,
                                                            "director": "Larry Semon",
                                                            "genre": [
                                                            "Comedy",
                                                            " Family",
                                                            " Fantasy",
                                                            " Adventure"
                                                            ],
                                                            "imdb_score": 5.3,
                                                            "name": "The Wizard of Oz"
                                                            }}, headers=header)
    assert response.status_code == 405



def test_add_movie_wrong_input():
    """
    Test function to test /add_movie endpoint without params
    """
    response = app.test_client().post('/add_movie', json={}, headers=header)
    assert response.status_code == 422

def test_add_movie():
    """
    Test function to test /add_movie endpoint
    """
    response = app.test_client().post('/add_movie', json={"movie_data": {"movie_name": "Sample Movie"}}, headers=header)
    assert response.status_code == 200

def test_remove_movie_wrong_input():
    """
    Test function to test /remove_movie without request params
    """
    response = app.test_client().delete('/remove_movie', json={}, headers=header)
    assert response.status_code == 422

def test_remove_movie():
    """
    Test function to test /remove_movie endpoint
    """
    response = app.test_client().delete('/remove_movie', json={"movie_name": "Sample Movie"}, headers=header)
    assert response.status_code == 200
