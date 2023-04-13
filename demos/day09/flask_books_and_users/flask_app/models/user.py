# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


DATABASE = "books"

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
    def get_one_with_books(cls, data):
        query = ""
        results = connectToMySQL(DATABASE).query_db(query,data)
        # a lot of confusing code goes here!!!
        return user