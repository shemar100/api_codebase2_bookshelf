# API BOOKSHELF 

This is a virtual bookshelf application, this is a fullstack application introduced by UDACITY as a part of the  fullstack nanodegree program. This lesson introduces industry implementation RESTful APIs implementation and Documentation. This project showcases implementation of well formatted API endpoints that leverages knowledge of HTTP practices and API development best practices.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

##  Getting Started

### Pre-requesites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.

#### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in this file.

To run the application, run the following command:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Thes commands put the application in development mode and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask Documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application will run on `http://localhost:5000/` and is a proxy in the front-end configuration.

#### Frontend

From the frontend folder, run the following command to start te client:
```
npm install // run command only once to  install dependencies for frontend
npm start
```

By default, the frontend will run on localhost:3000.

### Tests
In order to run tests navigate to the backend folder and run the following commands:

```
dropdb bookshef_test
createdb bookshef_test
psql bookshef_test < books.psql
python api_test.py
```

The first time you run the test, omit the drop db command.

All tests are kept in that file should be maintained as updates are made to app functionality.

### API Reference

### Getting Started
- Base URL: At present this app can only be run locally ans ia not hosted as a base URL. The backend app is hsoted at the default, `http:127.0.0.1:5000/`, which is set as a proxy in the frontend configuratiuon.
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:

```
{
    "success": True,
    "error": 400,
    "message": "bad request",
}
```
The API will return the return three error types:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable

### Endpoints
#### GET /books
- General:
    - Returns a list of book objects, success value, and total number of books.
    - Results are paginated in groups of 8. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/books`

```
{
  "books": [
    {
      "author": "shampoo", 
      "id": 17, 
      "rating": 2, 
      "title": "test title"
    }, 
    {
      "author": "shampoo", 
      "id": 18, 
      "rating": 2, 
      "title": "test title"
    }, 
    {
      "author": "suniel england", 
      "id": 23, 
      "rating": 7, 
      "title": "wuneil title"
    }, 
    {
      "author": "suniel england", 
      "id": 25, 
      "rating": 7, 
      "title": "wuneil title"
    }, 
    {
      "author": "suniel england", 
      "id": 27, 
      "rating": 7, 
      "title": "wuneil title"
    }, 
    {
      "author": "suniel england", 
      "id": 28, 
      "rating": 7, 
      "title": "wuneil title"
    }, 
    {
      "author": "suniel england", 
      "id": 30, 
      "rating": 1, 
      "title": "wuneil title"
    }, 
    {
      "author": "suniel england", 
      "id": 32, 
      "rating": 7, 
      "title": "wuneil title"
    }
  ], 
  "success": true, 
  "total_books": 95
}

```

#### POST /books
- General:
  - Creates a new book using submitted title, author, author and rating. Returns the id of the created book, success value, total books, and book list based on current page number to update frontend.
  - `curl http://127.0.0.1:5000/books -X POST -H "Content-Type: application/json" -d '{"title": "Test Title", "author": "John Doe", "rating": "5"}'`
```
{
  "books": [
    {
      "author": "John Doe", 
      "id": 1, 
      "rating": 5, 
      "title": "Test Title"
    }
  ], 
  "created": 1, 
  "success": true, 
  "total_books": 1
}
```
#### DELETE /books/{book_id}
- General:
  - Deletes the book of the given ID if exists. Returns the id of the deleted book, success value, total books, and book list based on current page number to update the frontend.
- `curl http://127.0.0.1:5000/books/1 -X DELETE`
```
{
  "books": [
    {
      "author": "Nick Foster", 
      "id": 2, 
      "rating": 5, 
      "title": "Test Title 2"
    }
  ], 
  "deleted": 1, 
  "success": true, 
  "total_books": 1
}

```
#### PATCH /books/{book_id}
- General:
  - If provided, updates the rating of the specified book. Returns the success value and id of the modified book.
  - `curl https://127.0.0.1/books/1`

  ```
  {
    "id": 1,
    "success": true
  }
  ```

## Deployment N/A

## Authors
Shemar Anderson, aka wizkid

# Acknowledgments
Thanks to udacity for the wonerful expeirence and the oppurtunity to test out new found full stack development skills.
