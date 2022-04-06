from .item import Item
class Clothing(Item):
    def __init__(self, condition = 0): # default arguments
        super().__init__(category = "Clothing", condition = condition) # keyword arguments


    def __str__(self):
        return "The finest clothing you could wear."