from .item import Item

class Clothing(Item):
    '''
    A sub-class of Item, indicating a type of item a vendor might have.
    
    Attributes:
        condition (float): optional descr. of item condition, 0 if not defined
        category (str): description of item category, always set to "Clothing"
    '''   

    def __init__(self, condition=0):
        '''
        Parameter: condition (float): optional description of item 
            condition, 0 if not defined
        '''

        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        '''Stringifies Clothing and returns a string describing the class.'''
        
        return "The finest clothing you could wear."