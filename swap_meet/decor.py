from .item import Item

class Decor(Item):
    '''
    Class that represents a decor item.
    
    ...

    Attributes
    - - - - - -
    category : str
    condition : int

    Methods
    -------
    str()
    condition.description()
    '''

    def __init__(self, condition = 0.0):
        '''
        Constructs attributes for Decor object from parent class; default values: category = "Decor", condition = 0.0.
        '''
        super().__init__(category = "Decor", condition = condition) 


    def __str__(self):
        '''
        Overrides parent str method and returns new string.
        '''
        return "Something to decorate your space."