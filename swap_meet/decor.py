from .item import Item

class Decor(Item):
    def __init__(self,category= None, condition = 0):
        if category is None:
            category = ""
        self.category = "Decor"
        if condition is 0:
            condition = 0
        self.condition = condition 

    def __str__(self):
        return "Something to decorate your space."