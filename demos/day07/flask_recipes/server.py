from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from recipe import Recipe
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


#! CREATE
@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['post'])
def create():
    print(request.form)
    Recipe.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    recipes = Recipe.get_all()
    print(recipes)
    return render_template('index.html', recipes = recipes)  # Return the string 'Hello World!' as a response

#! READ ONE
@app.route('/recipe/<int:id>')
def show(id):
    data = {'id': id}
    recipe = Recipe.get_recipe(data)
    print(recipe)
    return render_template('show.html', recipe = recipe)

#! UPDATE

#! DELETE 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.