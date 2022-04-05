from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, condition=None):
        self.category = "Clothing"
        if not condition:
            condition = 0
        self.condition = condition
    
    
    def __str__(self):
        return "The finest clothing you could wear."