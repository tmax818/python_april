from flask_app import app, render_template, redirect, request 
from flask_app.models.book import Book
from flask_app.models.user import User

#! CREATE
@app.route('/new')
def new():
    return render_template('books/new.html', users = User.get_all())

@app.route('/create', methods=['post'])
def create():
    print(request.form)
    Book.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/books')        
def books():
    books = Book.get_all()
    print(books)
    return render_template('books/index.html', books = books)  # Return the string 'Hello World!' as a response

#! READ ONE
@app.route('/books/<int:id>')
def show(id):
    book = Book.get_book(id)
    print(book)
    return render_template('books/show.html', book = book)


#! UPDATE

@app.route('/books/edit/<int:id>')
def edit_book(id):
    return render_template('books/edit.html', book = Book.get_book(id))

@app.route('/update', methods=['post'])
def update_book():
    print(request.form)
    Book.update(request.form)
    return redirect('/')

#! DELETE 
@app.route('/books/delete/<int:id>')
def destroy(id):
    data = {'id': id}
    Book.delete(id)
    return redirect('/books')