from mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'books'

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.author = data['author']
        self.title = data['title']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        return 'test'
            
