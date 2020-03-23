"""
Main Application script
"""
from dotenv import load_dotenv
load_dotenv()

import os
import json
import datetime
from flask import (Flask, Response, request)
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import services
import authenticate

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ['SECRET_KEY']
JWT = JWTManager(app)


@app.route('/')
def hello_world():
    """
    Home endpoint
    """
    return 'Hello, World!'


@app.route('/create_user', methods=['GET'])
def create_user():
    """
    Endpoint to create user
    """
    user = request.values.get('user_name')
    access_token = create_access_token({"user_name": user, "admin": False},
                                       expires_delta=datetime.timedelta(hours=2))
    response_body = services.get_response_body(api_key=access_token)
    return Response(response_body, status=200, mimetype='application/json')


@app.route('/create_admin', methods=['GET'])
def create_admin():
    """
    Endpoint to create admin user
    """
    super_user = request.headers.get('user_name')
    super_user_password = request.headers.get('password')
    if authenticate.authentic_user(super_user, super_user_password):
        user = request.values.get('admin_name')
        access_token = create_access_token({"user_name": user, "admin": True},
                                           expires_delta=datetime.timedelta(days=365))
        response_body = services.get_response_body(api_key=access_token)
        return Response(response_body, status=200, mimetype='application/json')
    response_body = services.get_response_body(err_msg="Invalid Credential")
    return Response(response_body, status=422, mimetype='application/json')


@app.route('/search_movie', methods=['GET'])
@jwt_required
def search_movie():
    """
    Endpoint to search movie
    """
    movie_name = request.values.get('movie_name')
    if not movie_name:
        response_body = services.get_response_body(msg="Invalid entry")
        return Response(response_body, status=422, mimetype='application/json')
    movie_data = services.get_movie_data(movie_name)
    return Response(json.dumps(movie_data), status=200, mimetype='application/json')


@app.route('/add_movie', methods=['POST'])
@jwt_required
def add_movie_endpoint():
    """
    Endpoint to add new movie entry
    """
    user_data = get_jwt_identity()
    if not user_data.get('admin'):
        response_body = services.get_response_body(msg="Unauthorized access")
        return Response(response_body, status=401, mimetype='application/json')
    movie_data = request.values.get('movie_data')
    if not movie_data:
        response_body = services.get_response_body(msg="Invalid entry")
        return Response(response_body, status=422, mimetype='application/json')
    movie_data = json.loads(movie_data)
    resp_status, resp_msg = services.insert_movie(movie_data)
    response_body = services.get_response_body(msg=resp_msg)
    return Response(response_body, status=resp_status, mimetype='application/json')


@app.route('/update_movie', methods=['PUT'])
@jwt_required
def update_movie_endpoint():
    """
    Endpoint to update movie entry
    """
    user_data = get_jwt_identity()
    if not user_data.get('admin'):
        response_body = services.get_response_body(msg="Unauthorized access")
        return Response(response_body, status=401, mimetype='application/json')
    movie_name = request.values.get('movie_name')
    movie_data = request.values.get('movie_data')
    if not movie_data or not movie_name:
        response_body = services.get_response_body(msg="Invalid entry")
        return Response(response_body, status=422, mimetype='application/json')
    movie_data = json.loads(movie_data)
    resp_status, resp_msg = services.update_movie(movie_name, movie_data)
    response_body = services.get_response_body(msg=resp_msg)
    return Response(response_body, status=resp_status, mimetype='application/json')


@app.route('/remove_movie', methods=['DELETE'])
@jwt_required
def remove_movie_endpoint():
    """
    Endpoint to delete movie entry for db
    """
    user_data = get_jwt_identity()
    if not user_data.get('admin'):
        response_body = services.get_response_body(msg="Unauthorized access")
        return Response(response_body, status=401, mimetype='application/json')
    movie_name = request.values.get('movie_name')
    if not movie_name:
        response_body = services.get_response_body(msg="Invalid entry")
        return Response(response_body, status=422, mimetype='application/json')
    resp_status, resp_msg = services.delete_movie(movie_name)
    response_body = services.get_response_body(msg=resp_msg)
    return Response(response_body, status=resp_status, mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ['PORT'])
    app.run(port=port, host='0.0.0.0')
