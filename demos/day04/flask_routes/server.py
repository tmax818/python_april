from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "<a href='/about'>about</a>"  # Return the string 'Hello World!' as a response

@app.route('/about')
def about():
    return "<h1>All about tyler</h1>"

@app.route('/hello/<name>')
def hello(name):
    return f"hello {name}"

@app.route('/hello/<name>/<int:num>')
def hello_repeat(name, num):
    return f"hello {name * num} {num}"

@app.route('/news')
def news():
    user = {'name': "maliq"}
    names = ['joan', 'maliq', 'zach', 'carl', 'tillman']
    number = 10
    return render_template("index.html", userjinja = user, number = number, names = names)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.