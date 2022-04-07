from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, condition=0,age=None):
        super().__init__("Clothing", condition, age)
        
    def __str__(self):
        return "The finest clothing you could wear."
