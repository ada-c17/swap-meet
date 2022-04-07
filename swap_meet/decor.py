from .item import Item

class Decor(Item):
    '''A sub-class of class Item, indicating a type of item a vendor might have.'''

    def __init__(self, condition=0):
        '''
        Parameters:
        condition (float): optional descr. of item condition, 0 if not defined

        Other attributes:
        category (str): description of item category, always set to "Decor"
        '''
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        '''Stringifies Decor and returns a string describing the class.'''
        return "Something to decorate your space."