from .item import Item

class Clothing(Item):
    
    def __init__(self, condition=0.0):
        """ Constructs all the necessary attributes for the item object. """
        self.category = "Clothing"
        self.condition = condition
    
    def __str__(self):
        """ Overrides string method. Returns "he finest clothing you could wear." """
        return "The finest clothing you could wear."