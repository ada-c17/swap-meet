from .item import Item

class Electronics(Item):
    '''A class that represents gadget items available to be swapped by vendors at the meet.
    
    Expects a 'condition' value (float), if none is supplied the item is assumed to be new (10.0)
    '''
    
    def __init__(self, condition=10.0):
        super().__init__(category = 'Electronics', condition = condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
