import requests

API = "KeBmM7FM3DYLHgDbomVvTbsupGgYmpcR"
class Tesla:
    
    CEO = "Elon Musk"
    all_teslas = []
    def __init__(self, model, color) -> None:
        self.model = model
        self.color = color
        Tesla.all_teslas.append(self)
            
    
    @classmethod
    def get_CEO(cls):
        return cls.CEO
    
    @classmethod
    def get_all_teslas(cls):
        for tesla in cls.all_teslas:
            print(tesla)
            
    @staticmethod
    def get_stock_quote(ticker):
        quote = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2023-03-01/2023-03-01?adjusted=true&sort=asc&limit=120&apiKey={API}").json()
        print(quote)
    
    
    
t = Tesla("s", "red")
t1= Tesla("3", "blue")
t2 = Tesla("x", "green")