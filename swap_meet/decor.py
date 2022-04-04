from .item import Item

class Decor(Item):
    
    def __init__(self, condition=0.0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space." 
