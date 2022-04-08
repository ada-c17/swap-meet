from .item import Item
class Electronics(Item):
    def __init__(self, condition = 0): # default arguments
        super().__init__(category = "Electronics", condition = condition) # keyword arguments

    def __str__(self):
        return "A gadget full of buttons and secrets."


