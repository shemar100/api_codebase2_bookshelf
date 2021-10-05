import unittest
import json
from flaskr import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    """ This class represents the resource test case """

    def setUp(self):
        """ Define test variables and intialize app """
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf"
        self.database_path = "postgres://{}:{}@{}/{}".format("postgres","Hotskull!000", "localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Book 1',
            'author': 'Barry B.B.B.B.B',
            'rating': 1
        }

    def tearDown(self):
        """ Executed after each test"""
        pass

    def test_get_paginated(self):
        res = self.client().get('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])
        self.assertTrue(data['books'])

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/books?page=1000', json={'rating': 1})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_update_book_rating(self):
        res = self.client().patch('/books/30', json={'rating': 1})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 30).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(book.format()['rating'], 1)

    def test_400_for_failed_update(self):
        res = self.client().patch('/books/5')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request' )
        
if __name__ == "__main__":
    unittest.main()