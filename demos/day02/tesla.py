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
        
def drive(tesla):
    tesla.drive()
    

tylers_tesla = Tesla('modelx', 'red', True)
hirals_tesla = Tesla("model3", 'blue', False)
drive(tylers_tesla)
     
hirals_tesla.drive()
hirals_tesla.drive()


print(tylers_tesla)