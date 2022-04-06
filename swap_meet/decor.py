from .item import Item

class Decor(Item):
    def __init__(self, condition = 0.0):
        '''
        Constructs attributes for Decor object from parent class; default values: category = "Decor", condition = 0.0.
        '''
        super().__init__(condition = condition, category = "Decor") 


    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "Something to decorate your space."