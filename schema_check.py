from marshmallow import Schema, fields

class CreateUserInputSchema(Schema):
    """
    /creat_user - GET
    Parameters:
        - user_name (str)
    """
    user_name = fields.Str(required=True, allow_none=False)

class SearchMovieInputScheme(Schema):
    """
    /search_movie - GET
    Parameters:
        - movie_name (str)
    """
    movie_name = fields.Str(required=True, allow_none=False)

class AddMovieInputScheme(Schema):
    """
    /add_movie - POST
    Parameters:
        - movie_data (dict)
    """
    movie_data = fields.Dict(keys=fields.Str(), required=True)

class UpdateMovieInputScheme(Schema):
    """
    /add_movie - POST
    Parameters:
        - movie_data (dict)
    """
    movie_name = fields.Str(required=True, allow_none=False)
    movie_data = fields.Dict(required=True)

class RemoveMovieInputScheme(Schema):
    """
    /add_movie - POST
    Parameters:
        - movie_data (dict)
    """
    movie_name = fields.Str(required=True, allow_none=False)
