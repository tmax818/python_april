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
```

- [ ] start application by running:

```
python server.py
```

- [ ] go to [localhost:5000](http://localhost:5000/)

- [ ] create a [templates](templates/index.html) folder that contains our HTML

## Connect to a database

- [ ] create ERD: ![](book_schema.png)
- [ ] install the module to connect Flask to mysql:

```bash
[python -m] pipenv install pymysql
```

- [ ] create [mysqlconnection.py](mysqlconnection.py)
- [ ] create [book.py](book.py)