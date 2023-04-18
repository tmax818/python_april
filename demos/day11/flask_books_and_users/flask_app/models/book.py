# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


DATABASE = "books_belt_demo"

class Book:
    
    
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.thoughts = data['thoughts']
        self.date_read = data['date_read']
        self.finished = data['finished']
        self.user = data['first_name']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def show_title(self):
        return self.title
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, author,thoughts, date_read, finished, user_id) VALUES (%(title)s, %(author)s,%(thoughts)s, %(date_read)s, %(finished)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
       
    #! READ ALL 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books JOIN users ON users.id = books.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        books = []
        for book_dict in results:
            books.append(cls(book_dict))
        return books
    
    #! READ ONE
    @classmethod
    def get_book(cls, id):
        query = "SELECT * FROM books JOIN users ON users.id = books.user_id WHERE books.id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result[0])
        book = Book(result[0])
        return book
    
    #! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE books SET title=%(title)s, author=%(author)s, thoughts=%(thoughts)s,finished=%(finished)s, date_read=%(date_read)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #! DELETE
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM books WHERE id = %(id)s;"
        data = {
            'id':id
        }
        return connectToMySQL(DATABASE).query_db(query, data)
        
