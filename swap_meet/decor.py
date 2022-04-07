from swap_meet.item import Item

class Decor(Item):
    '''
    Decor class is the child class of Item class that inherits methods for condition of decor.
    '''
    
    def __init__(self, condition = 0):
        '''
        Inherits Item methods.
        '''
        super().__init__(condition = condition, category = "Decor")

    def __str__(self):
        '''
        Returns this string when printing this class.
        '''
        return "Something to decorate your space."
    
