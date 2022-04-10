from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0, age = 0):
        super().__init__(category = "Clothing", condition = condition, age = age)
        
    def __str__(self):
        return "The finest clothing you could wear."

    
