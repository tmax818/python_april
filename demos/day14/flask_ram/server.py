from flask import Flask, render_template
import requests
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    data = requests.get("https://rickandmortyapi.com/api").json()
    print(data)
    return render_template('index.html', data = data)

@app.route('/<var>')
def characters(var):
    data = requests.get(f"https://rickandmortyapi.com/api/{var}").json()
    pprint(data['results'])
    return render_template('index.html', characters = data['results'])

@app.route('/search/<name>')
def search(name):
    data = requests.get(f"https://rickandmortyapi.com/api/character/?name={name}").json()
    return render_template('result.html', data = data)


if __name__ == '__main__':
    app.run(debug=True)
