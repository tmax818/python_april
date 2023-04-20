from flask import Flask, render_template
import requests
from pprint import pprint
app = Flask(__name__)
url = "https://rickandmortyapi.com/api"

@app.route("/")
def index():
    data = requests.get("https://rickandmortyapi.com/api").json()
    print(data)
    return render_template('index.html')

@app.route("/url/<url>")
def handle_url(url):
    data = requests.get(url).json()
    print(data)
    return render_template('index.html')

@app.route("/<var>")
def episode(var):
    data = requests.get(f"https://rickandmortyapi.com/api/").json()
    pprint(data)
    return render_template('index.html', data = data)

@app.route("/<endpoint>/<int:id>")
def show(endpoint, id):
    data = requests.get(f"https://rickandmortyapi.com/api/{endpoint}/{id}").json()
    pprint(data)
    return render_template('show.html', data = data)

@app.route("/api/")
def api_index():
    data = requests.get("https://rickandmortyapi.com/api").json()
    print(data)
    return data

@app.route("/api/<endpoint>")
def api_endpoint(endpoint = ""):
    string = url + endpoint
    data = requests.get(f"https://rickandmortyapi.com/api/{endpoint}").json()
    print(data)
    return data



if __name__ == "__main__":
    app.run(debug=True)