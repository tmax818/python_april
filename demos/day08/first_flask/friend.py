# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
from pprint import pprint
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def say_hello(self):
        return f"Hi my name is {self.first_name}"

    #! CREATE
    @classmethod
    def save(cls, data):
        pass

    # Now we use class methods to query our database
    #! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # results is a list of dictionaries
        pprint(results)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
            
