import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import select  # , or_
from flask_cors import CORS
from models import setup_db, Book

BOOKS_PER_SHELF = 8

def paginate_books(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF
    books = Book.query.all()
    formatted_books = [book.format() for book in selection]
    current_book = formatted_books[start:end]

    return current_book

# @TODO: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    @app.route('/books')
    def books():
        selection = Book.query.order_by(Book.id).all()
        current_book = paginate_books(request, selection)

        if len(selection) == 0:
            abort(404)

        return jsonify({
            'success' : True,
            'books': current_book,
            'total_books': len(Book.query.all()),
        })
    @app.route('/books/<int:book_id>')
    def specific_books(book_id):
        book =  Book.query.filter(Book.id == book_id).one_or_none()
        if book is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'book': book.format()
            })

    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_book(book_id):
        body = request.get_json()

        try:
            book = Book.query.filter(Book.id == book_id).one_or_none()
            if book is None:
                abort(404)
            if 'rating' in body:
                book.rating = int(body.get('rating'))

            book.update()
            return jsonify({
                'success': True,
                'id': book.id
            })

        except:
            abort(400)
        
    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_books(book_id):
        try:
            book = Book.query.filter(Book.id == book_id).one_or_none()
            if book is None:
                abort(400)
                
            book.delete()
            selection = Book.query.order_by(Book.id).all()
            current_books = paginate_books(request, selection)

            return jsonify({
                'success' : True,
                'deleted': book.id,
                'books': current_books,
                'total_books': len(Book.query.all())
            })
        except:
            abort(422)
            
    @app.route("/books", methods=['POST'])
    def create_book():
        body = request.get_json()
        new_title = body.get('title')
        new_author = body.get('author')
        new_rating = body.get('rating')

        try:
            book = Book(new_title, new_author, new_rating)
            book.insert()
            selection = Book.query.order_by(Book.id).all()
            current_books = paginate_books(request, selection)

            return jsonify({
                'success': True,
                'created': book.id,
                'books' : current_books,
                'total_books': len(Book.query.all()),
            })
        except:
            abort(422)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "Not found"
            }), 404

    @app.errorhandler()
    def unprocessable(error):
        return jsonify({
         "success": False, 
        "error": 422,
        "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
        "success": False, 
        "error": 400,
        "message": "bad request"
        }), 400


    return app
