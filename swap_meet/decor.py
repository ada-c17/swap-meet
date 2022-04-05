from .item import Item

class Decor(Item):
    def __init__(self, condition=0):
        Item.__init__(self, category = "Decor", condition = condition)

    def __str__(self):
        return "Something to decorate your space."