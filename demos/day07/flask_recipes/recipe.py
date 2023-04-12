# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = "recipes_schema"

class Recipe:
    
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.chef = data['chef']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def show_name(self):
        return self.name
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, chef) VALUES (%(name)s, %(chef)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
       
    #! READ ALL 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        recipes = []
        for recipe_dict in results:
            recipes.append(cls(recipe_dict))
        return recipes
    
    #! READ ONE
    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result[0])
        recipe = Recipe(result[0])
        return recipe
        
