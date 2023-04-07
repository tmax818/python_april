from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
app = Flask(__name__)
app.secret_key = "any string you want"

languages = ["python", "java", "c", "javascript", "ruby"]

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', languages = languages)  

@app.route('/handle_form', methods=['POST'])
def create():
    ## code to process data from form
    print(request.form)
    session['name'] = request.form['name']
    session['language'] = request.form['language']
    return redirect('/show') # always redirect to a route!!!

@app.route('/show')
def show():
    return render_template('show.html')

## MORE ROUTES HERE 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.