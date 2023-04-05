# from the players file import the players list
from players import players
from pprint import pprint

class Player:
    # def __init__(self, name, age, position, team):
    #     self.name = name
    #     self.age = age
    #     self.position = position
    #     self.team = team
    
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
        
    def __repr__(self) -> str:
        return f"{self.name} is {self.age} years old and plays for {self.team}"

        
    def shoot(self):
        print(f"{self.name} shoots the ball")
  
new_player_list = []

for player in players:
    temp_player = Player(player)
    new_player_list.append(temp_player)
    



        
# print(players[0]['name'])

player1 = Player(players[0])
print(new_player_list)