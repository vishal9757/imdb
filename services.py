"""
Service layer script file
"""
import os
import json
from pymongo import MongoClient
import pymongo
import config

MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = int(os.environ['MONGO_PORT'])
MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')

def get_mongo_connection():
    """
    Function to create mongo connection
    Args:
    Return:
        client (Mongo client)
    """
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    if MONGO_USER and MONGO_PASSWORD:
        client.admin.authenticate(MONGO_USER, MONGO_PASSWORD)
    return client


def insert_movie(movie_data):
    """
    Function to insert movie data into database
    Args:
        movie_data(dict): movie tobe inserted
    Return:
        status(int): status code\
        msg(str)
    """
    client = get_mongo_connection()
    try:
        client[config.MOVIE_DB][config.MOVIE_COLLECTION].insert_one(movie_data)
        return 200, "Successfully Inserted"
    except pymongo.errors.DuplicateKeyError as error_msg:
        return 422, str(error_msg)


def update_movie(movie_name, movie_data):
    """
    Function to insert movie data into database
    Args:
        movie_data(dict): movie tobe inserted
    Return:
        status(int): status code
        msg(str)
    """
    client = get_mongo_connection()
    try:
        client[config.MOVIE_DB][config.MOVIE_COLLECTION].update_one(
            {"name": movie_name}, {"$set": movie_data})
        return 200, "Updated"
    except Exception as error:
        return 400, str(error)


def delete_movie(movie_name):
    """
    Function to remove movie data from database
    Args:
        movie_name(str): movie to be deleted
    Return:
        status(int): status code
        msg(str)
    """
    client = get_mongo_connection()
    try:
        client[config.MOVIE_DB][config.MOVIE_COLLECTION].delete_one(
            {"name": movie_name})
        return 200, "Removed"
    except Exception as error:
        return 400, str(error)


def get_movie_data(movie_name):
    """
    Function to get movie name from database
    Args:
        movie_name(str): name of movie to search
    Return:
        document(dict): movie document
    """
    client = get_mongo_connection()
    document = client[config.MOVIE_DB][
        config.MOVIE_COLLECTION].find_one({"name": movie_name}, {"_id": 0})
    return document


def get_response_body(**kwargs):
    """
    Function to get text response format of the given key-value arguments
    Args:
        **kwargs
    Output:
        response_body(str): json dumps of key-value arguments
    """
    response_body = {}
    for key, value in kwargs.items():
        response_body[key] = value
    response_body = json.dumps(response_body)
    return response_body
