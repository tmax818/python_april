# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = "books_schema"

class Book:
    
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        books = []
        for book in results:
            books.append(Book(book))
        return books
