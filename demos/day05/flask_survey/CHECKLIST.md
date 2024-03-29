# checklist

- [x] create a new directory
- [ ] inside the directory create virtural env by running:

```bash
[python -m] pipenv install flask
```

- [ ] activate the virtual env every time you open a new terminal:

```bash
[python -m] pipenv shell 
```

- [ ] create [server.py](server.py)

```py
from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
app = Flask(__name__)
app.secret_key = "any string you want"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/handle_form', methods=['POST'])
def create():
    ## code to process data from form
    return redirect('/') # always redirect to a route!!!

@app.route('/show')
def show():
    return render_template('show.html')

## MORE ROUTES HERE 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
```

- [ ] start application by running:

```
python server.py
```

- [ ] go to [localhost:5000](http://localhost:5000/)

- [ ] create a [templates](templates/index.html) folder that contains our HTML