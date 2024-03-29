from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from book import Book
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


#! CREATE
@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['post'])
def create():
    print(request.form)
    Book.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    books = Book.get_all()
    print(books)
    return render_template('index.html', books = books)  # Return the string 'Hello World!' as a response

#! READ ONE
@app.route('/book/<int:id>')
def show(id):
    book = Book.get_book(id)
    print(book)
    return render_template('show.html', book = book)


#! UPDATE

@app.route('/book/edit/<int:id>')
def edit_book(id):
    return render_template('edit.html', book = Book.get_book(id))

@app.route('/update', methods=['post'])
def update_book():
    print(request.form)
    Book.update(request.form)
    return redirect('/')

#! DELETE 
@app.route('/book/delete/<int:id>')
def destroy(id):
    Book.delete(id)
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.