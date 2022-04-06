from .item import Item

class Decor(Item):
    
    def __init__(self, condition=0.0):
        """ Constructs all the necessary attributes for the item object. """
        super().__init__(category="Decor", condition=condition)

    def __str__(self):
        """ Overrides string method. Returns "Something to decorate your space." """
        return "Something to decorate your space." 
