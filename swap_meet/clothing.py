from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0):
        self.category = "Clothing"
        self.condition = condition #is there a way to not have to repeat this line
    
    def __str__(self):
        return "The finest clothing you could wear."