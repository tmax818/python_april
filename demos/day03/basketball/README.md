# Basketball Dictionaries


### Tyler's added challenge:

- [ ] Create a new file: [players.py](players.py) to hold the players list.

## tasks

- [ ] Set up a new [file](player.py) and add the Player class with the given constructor:

```py
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
```


- [ ] Challenge 1: Update the constructor to accept a dictionary (data) as an argument and set the attributes using the dictionary

- [ ] Complete challenge 2: Create 3 instances of the Player class using the list from [players.py](players.py)

- [ ] Complete challenge 3: Populate a new list with Player instances from the list of players.

- [ ] Ninja Bonus: Add a `@classmethod` called `get_team(cls, team_list)` that, given a list of dictionaries populates and returns a new list of Player objects.