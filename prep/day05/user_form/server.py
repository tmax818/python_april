from flask import Flask, render_template, redirect, request, session
from user import User
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "i invented quotation fingers!!"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/users', methods=['post'])
def create_user():
    print(request.form)
    session['user_name'] = request.form['user_name']
    User(request.form)
    print(User.all_users)
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')
    

## MORE ROUTES HERE 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  