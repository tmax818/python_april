# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.book import Book
from flask_app import flash

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = "books_belt_demo"

class User:
    
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #! READ ALL 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        users = []
        for user_dict in results:
            users.append(cls(user_dict))
        return users
    
    #! READ ONE
    @classmethod
    def get_one_with_books(cls, id):
        # a lot of confusing code goes here!!!
        query = "SELECT * FROM users JOIN books ON users.id = books.user_id WHERE users.id = %(id)s;"
        # data = {'id':id}
        results = connectToMySQL(DATABASE).query_db(query,{'id': id})
        pprint(results)
        user = User(results[0])
        print(user.books)
        for item in results:
            pprint(item)
            temp_book = {
                'id': item['books.id'],
                'title': item['title'],
                'author': item['author'],
                'user_id': item['user_id'],
                'created_at': item['books.created_at'],
                'updated_at': item['books.updated_at']              
            }
            user.books.append(Book(temp_book))
        return user
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def find_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {'email': email}
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) > 0:
            user = User(result[0])
            return user
        else:
            return False
            
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            is_valid = False
            flash("first name must be at least 2 chars")
        if len(user['last_name']) < 4:
            is_valid = False
            flash("last name must be at least 4 chars")
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash("passwords must match")
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
        