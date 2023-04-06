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
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
        
    def __repr__(self) -> str:
        return f"{self.name} is {self.age} years old and plays for {self.team}"

        
    def shoot(self):
        print(f"{self.name} shoots the ball")
        
    @classmethod
    def make_player_list(cls, players):
        player_list = []
        for player in players:
            player_list.append(cls(player))
        return player_list
    
    @classmethod
    def make_player(cls, player):
        return cls(player)
  
