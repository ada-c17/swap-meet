from .item import Item

class Decor(Item):

    def __init__(self, category="Decor", condition=0, age=None):
        super().__init__(category, condition, age)
    
    def __str__(self):
        return "Something to decorate your space."