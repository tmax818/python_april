from flask_app import app, render_template, redirect, request 
from flask_app.models.book import Book
from flask_app.models.user import User

#! CREATE
@app.route('/new')
def new():
    return render_template('new.html', users = User.get_all())

@app.route('/create', methods=['post'])
def create():
    print(request.form)
    Book.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/')        
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