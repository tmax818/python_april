from flask import Flask, render_template
import requests
from pprint import pprint
app = Flask(__name__)

@app.route('/')
def index():
    data = requests.get("https://rickandmortyapi.com/api").json()
    print(data['characters'])
    return render_template('index.html')

@app.route('/character')
def character():
    characters = requests.get("https://rickandmortyapi.com/api/character").json()
    pprint(characters)
    return render_template('index.html', characters = characters['results'])
    


if __name__ == '__main__':
    app.run(debug=True)