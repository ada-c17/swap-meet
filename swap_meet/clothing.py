from swap_meet.item import Item

class Clothing(Item):
    '''
    Clothing class is the child class of Item class that inherits methods for condition of the clothing.
    '''
    
    def __init__(self, condition = 0):
        '''
        Inherits Item methods.
        '''
        super().__init__(condition = condition, category = "Clothing")


    def __str__(self):
        '''
        Returns this string when printing this class.
        '''
        return "The finest clothing you could wear."

    

    