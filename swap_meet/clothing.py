from .item import Item

class Clothing(Item):
    '''A class that represents wearable items available to be swapped by vendors at the meet.
    
    Expects a 'condition' value (float), if none is supplied the item is assumed to be new (10.0)
    '''

    def __init__(self, condition = 10.0):
        super().__init__(category = 'Clothing', condition = condition)

    def __str__(self):
        return "The finest clothing you could wear."