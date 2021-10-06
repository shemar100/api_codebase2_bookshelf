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

###Endpoints
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
