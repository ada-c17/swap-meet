from .item import Item

class Decor(Item):
    def __init__(self, category = "Decor", condition = 0.0):
        '''
        Constructs attributes for Decor object, default values: category = "Decor", condition =0.
        '''
        self.category = category
        self.condition = condition

    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "Something to decorate your space."