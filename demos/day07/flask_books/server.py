from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from book import Book
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    books = Book.get_all()
    print(books)
    return render_template('index.html', books = books)  # Return the string 'Hello World!' as a response

## MORE ROUTES HERE 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.