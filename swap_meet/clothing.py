from .item import Item

class Clothing(Item):
    '''
    Class that represents a clothing item.
    
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
        Constructs attributes for Clothing object from parent class; default values: category = "Clothing", condition = 0.0.
        '''
        super().__init__(category = "Clothing", condition = condition)
        
    def __str__(self):
        '''
        Overrides parent str method and returns new string.
        '''
        return "The finest clothing you could wear."
