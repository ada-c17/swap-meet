from swap_meet.item import Item

class Decor(Item):
    '''
    A class to represent a decor item.
    Child class of Item class
    '''
    def __init__(self, condition = 0.0):
        super().__init__(condition = condition, category="Decor")
        
        
    def __str__(self):
        return "Something to decorate your space."

    