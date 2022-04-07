from .item import Item

class Decor(Item):

    def __init__(self, condition=None):
        self.category  = "Decor"
        self.condition = condition
        self.message = "Something to decorate your space."

    
