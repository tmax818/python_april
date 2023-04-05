# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

from players import players
from pprint import pprint

class Player:
    
    new_team = []
    
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
        
    @classmethod
    def get_team(cls, team_list):
        for player in team_list:
            cls.new_team.append(cls(player))
        return cls.new_team
            

pprint(players[0])

kevin = Player(players[0])
jason = Player(players[1])
kyrie = Player(players[2])

player_objects = Player.get_team(players)
