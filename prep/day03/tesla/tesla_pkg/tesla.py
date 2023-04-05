import requests
from tesla_pkg.api import API

class Tesla:
    # attributes aka qualities, adjectives
    
    all_teslas = []
    CEO = "Elon Musk"
    
    def __init__(self, model, color, autopilot):
        self.model = model
        self.color = color
        self.mileage = 0
        self.charge = 100
        self.autopilot = autopilot
        Tesla.all_teslas.append(self)

        
    # instance methods
    def drive(self):
        self.mileage += 10
        self.charge -= 1
        if self.autopilot:
            print(f"My {self.color} {self.model} is driving itself!! The mileage is now {self.mileage}")
        else:
            print(f"I am driving my {self.color} {self.model} and the mileage is now {self.mileage}")
            
    @classmethod
    def get_all_teslas(cls):
        for tesla in cls.all_teslas:
            print(f"This tesla is a {tesla.model} its color is {tesla.color}.")
            
    @staticmethod
    def get_stock_quote(ticker):
        quote = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2023-03-01/2023-03-01?adjusted=true&sort=asc&limit=120&apiKey={API}").json()
        print(quote)
        