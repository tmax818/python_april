from flask import Flask, render_template
from players import players as players_list
from player import Player
app = Flask(__name__)    

@app.route('/')         
def index():
    players = Player.make_player_list(players_list)
    return render_template("index.html", players = players)

@app.route('/show/<int:id>')
def show(id):
    player = Player.make_player(players_list[id])
    return render_template("show.html", player = player)



if __name__=="__main__":    
    app.run(debug=True)    

