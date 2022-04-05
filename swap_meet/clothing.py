from .item import Item

class Clothing(Item):
    def __init__(self,category= None, condition = 0):
        if category is None:
            category = ""
        self.category = "Clothing"
        if condition is 0:
            condition = 0
        self.condition = condition 

    def __str__(self):
        return "The finest clothing you could wear."
