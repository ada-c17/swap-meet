from .item import Item

class Decor(Item):
    def __init__(self,condition=0,age=float("inf")):
        super().__init__("Decor",condition,age)

    def __str__(self):
        return "Something to decorate your space."