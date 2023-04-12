from flask import Flask, render_template, redirect, request
from friend import Friend # import the class from friend.py
app = Flask(__name__)

#! CREATE

@app.route("/new")
def new():
    return render_template('new.html')

@app.route("/create", methods=['post'])
def create_friend():
    print(request.form)
    return redirect('/')


#! READ ALL
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends = friends)

#! READ ONE

#! UPDATE

#! DELETE
            
if __name__ == "__main__":
    app.run(debug=True)

