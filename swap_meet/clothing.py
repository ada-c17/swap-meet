from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0.0):
        '''
        Constructs attributes for Clothing object from parent class; default values: category = "Clothing", condition =0.
        '''
        super().__init__(condition = condition, category = "Clothing")
    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "The finest clothing you could wear."
