# imdb

1. Create User

    **Description**: This endpoint is to get Bearer API token

    **Path**: `/create_user

    **Method**: GET

    **Status**: 200
    
    **Request Parameter**:
    {
      "user_name": "XYZ0"
    }

    **Success response**:
    {
      "api_key": Token
    }


2. Search Movie

    **Description**: This endpoint retrieves the search movie result

    **Path**: `/search_movie

    **Method**: GET

    **Status**: 200
    
    **Request Parameter**:
    {
      "movie_name": "The Wizard of Oz"
    }

    **Success response**:
    {
      "99popularity" : 83,
      "director" : "Victor Fleming",
      "genre" : [
        "Adventure",
        " Family",
        " Fantasy",
        " Musical"
      ],
      "imdb_score" : 8.3,
      "name" : "The Wizard of Oz"
    }

3. Add Movie

    **Description**: This endpoint is to add new movie entry in Database (needs Admin access)

    **Path**: `/add_movie

    **Method**: POST

    **Status**: 200
    
    **Request Parameter**:
    {
      "movie_data": {
        "99popularity": 83,
        "director": "Victor Fleming",
        "genre": [
          "Adventure",
          " Family",
          " Fantasy",
          " Musical"
        ],
        "imdb_score": 8.3,
        "name": "The Wizard of Oz"
      }
    }

    **Success response**:
    {
      "msg" : "Successfully Inserted"
    }
  
4. Update Movie
    **Description**: This endpoint is to update movie record (needs Admin access)

    **Path**: `/update_movie

    **Method**: PUT

    **Status**: 200
    
    **Request Parameter**:
    {
      "movie_name": "The Wizard of Oz",
      "movie_data": {
          "99popularity": 83,
          "director": "Victor Fleming",
          "genre": [
            "Adventure",
            " Family",
            " Fantasy",
            " Musical"
          ],
          "imdb_score": 8.3,
          "name": "The Wizard of Oz"
        }
    }

    **Success response**:
    {
      "msg" : "Updated"
    }

5. Remove Movie
    **Description**: This endpoint is to delete movie record (needs Admin access)

    **Path**: `/remove_movie

    **Method**: DELETE

    **Status**: 200
    
    **Request Parameter**:
    {
      "movie_name" : "The Wizard of Oz"
    }

    **Success response**:
    {
      "msg" : "Removed"
    }
