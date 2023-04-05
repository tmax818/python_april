class Main:
    
    
    def __init__(self, attr1) -> None:
        self.attr1 = attr1
        
    def __repr__(self):
        return f"{self.attr1}"
    
inst = Main("attribute")