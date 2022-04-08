from swap_meet.item import Item


class Clothing(Item):

    
    def __init__(self, condition = 0, age = None):
        self.category = "Clothing"
        self.condition = condition
        self.age = age
    

    #override str() for Clothing, returns "The finest clothing you could wear."
    def __str__(self):
        return "The finest clothing you could wear."