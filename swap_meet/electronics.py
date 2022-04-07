from swap_meet.item import Item

class Electronics(Item):
    '''
    Electronics class is the child class of Item class that inherits methods for condition of electronics.
    '''
    
    def __init__(self, condition = 0):
        '''
        Inherits Item methods.
        '''
        super().__init__(condition = condition, category = "Electronics")

    def __str__(self):
        '''
        Returns this string when printing this class.
        '''
        return "A gadget full of buttons and secrets."
