from flask_app import app, render_template, redirect, request 
from flask_app.models.user import User

@app.route('/users')
def users():
    return render_template('users.html', users = User.get_all())

@app.route('/users/<int:id>')
def show_user(id):
    user = User.get_one_with_books(id)
    print(user.books)
    return render_template('show_user.html', user = user)
