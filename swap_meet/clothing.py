from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, condition = 0):
        self.category = "Clothing"
        self.condition = condition
    
    
    def __str__(self):
        super().__str__()
        return "The finest clothing you could wear."