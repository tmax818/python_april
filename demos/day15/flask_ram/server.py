from flask import Flask, render_template, request, redirect, jsonify
import requests
from pprint import pprint
app = Flask(__name__)
APIkey = "61107cb5aeddc3fe473d540e1768ff09"
lat = 35.221996
lon = -101.831299

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

@app.route('/search', methods = ['post'])
def search():
    print(request.form)
    res = requests.get(f"https://rickandmortyapi.com/api/character/?name={request.form['name']}").json()
    print(res)
    return render_template('index.html', res = res['results'])

@app.route('/weather')
def weather():
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}").json()
    print(data)
    return redirect('/')

@app.route('/api/info')
def info():
    person = {'name': 'zach', 'age': 23}
    return jsonify(person)
    


if __name__ == '__main__':
    app.run(debug=True)