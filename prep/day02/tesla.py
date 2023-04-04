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
    
    
    
t = Tesla("s", "red")
t1= Tesla("3", "blue")
t2 = Tesla("x", "green")