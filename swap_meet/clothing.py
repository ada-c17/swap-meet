from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, condition = "", age = 0):
        self.category = "Clothing"
        self.condition = condition
        self.age = age

    # stringify method for Clothing
    def __str__(self):
        return "The finest clothing you could wear."