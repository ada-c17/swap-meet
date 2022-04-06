from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0.0, category = "Clothing"):
        '''
        Constructs attributes for Clothing object, default values: category = "Clothing", condition =0.
        '''
        self.category = category
        self.condition = condition 

    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "The finest clothing you could wear."
