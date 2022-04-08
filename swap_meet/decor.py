from .item import Item
class Decor(Item):
    def __init__(self, condition = 0): # default arguments
        super().__init__(category = "Decor", condition = condition) # keyword arguments

    def __str__(self):
        return "Something to decorate your space."