class Tesla:
    # attributes aka qualities, adjectives
    def __init__(self, model, color, autopilot):
        self.model = model
        self.color = color
        self.mileage = 0
        self.charge = 100
        self.autopilot = autopilot

        
    # instance methods
    def drive(self):
        self.mileage += 10
        print(f"I am driving my {self.color} {self.model} and the mileage is now {self.mileage}")
        
# tylers_tesla = Tesla("modelx", "red", True)
        
class Owner:
    
    def __init__(self, name, keyFob, model):
        self.name = name
        self.keyFob = keyFob
        self.tesla = Tesla(model, "red", True)
        
tyler = Owner("Tyler", True, "modelX")
        
    
        
    
    