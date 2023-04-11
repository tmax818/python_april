from flask import Flask, render_template
from book import Book
app = Flask(__name__)

@app.route("/")
def index():
    books = Book.get_all()
    print(books)
    return render_template("index.html")
            
if __name__ == "__main__":
    app.run(debug=True)

