from .item import Item

class Clothing(Item):
    '''A sub-class of class Item, indicating a type of item a vendor might have.'''   

    def __init__(self, condition=0):
        '''
        Parameters:
        condition (float): optional descr. of item condition, 0 if not defined

        Other attributes:
        category (str): description of item category, always set to "Clothing"
        '''
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        '''Stringifies Clothing and returns a string describing the class.'''
        return "The finest clothing you could wear."