from tesla_pkg.tesla import Tesla

class Owner:
    
    def __init__(self, name, keyFob, model, autopilot=False):
        self.name = name
        self.keyFob = keyFob
        self.tesla = Tesla(model, "red", autopilot)
        
    def drive_my_tesla(self):
        self.tesla.drive()
        


    
        
    
    