# API movies
## Movies API
This API is an interface for managing a collection of movies, which can be used to search for, add, update, and delete movies. It is based on the FastAPI framework and is implemented using the routing pattern.

## Usage
The API can be used by sending HTTP requests to the corresponding routes. The following routes have been implemented:

### GET /movies
Returns a list of all movies in the database.

Query parameters:

None
### GET /movies/{id}
Returns a specific movie in the database.

Path parameters:

id: numeric identifier of the movie to retrieve.
### GET /movies
Returns a list of all movies in the database that match the specified category.

Query parameters:

category: the category of movies to retrieve.
### POST /movies
Adds a new movie to the database.

Body parameters:

movie: a structure describing the movie to add.
### PUT /movies/{id}
Updates a specific movie in the database.

Path parameters:

id: numeric identifier of the movie to update.
Body parameters:

movie: a structure describing the movie to update.
### DELETE /movies/{id}
Deletes a specific movie from the database.

Path parameters:

id: numeric identifier of the movie to delete.
Authentication
Some routes require an authentication token that can be obtained by sending a POST request to the /login route.

### POST /login
Authenticates the user and returns an access token.

Body parameters:

username: the username of the user.
password: the password of the user.
## Responses
API responses are sent in JSON format, and the corresponding HTTP status codes are used. The exact format of the responses depends on the route being used, and is specified in the corresponding documentation.

## Installing the requirements 
``` pip install -r requirements.txt ```

## Execute
``` uvicorn main:app ```
