from .item import Item

class Electronics(Item):
    
    def __init__(self, condition=0.0):
        """ Constructs all the necessary attributes for the item object. """
        super().__init__(category="Electronics", condition=condition)
    
    def __str__(self):
        """ Overrides string method. Returns "A gadget full of buttons and secrets" """
        return "A gadget full of buttons and secrets." 