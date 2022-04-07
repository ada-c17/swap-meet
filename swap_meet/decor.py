from .item import Item

class Decor(Item):
    '''A class that represents items used to brighten up spaces which are available to be swapped by vendors at the meet.
    
    Expects a 'condition' value (float), if none is supplied the item is assumed to be new (10.0)
    '''
    
    def __init__(self, condition = 10.0):
        super().__init__(category = 'Decor', condition = condition)

    def __str__(self):
        return "Something to decorate your space."