from .item import Item

class Electronics(Item):
    '''
    Class that represents an electronic item.

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
        Constructs attributes for Electronics object from parent class, default values: category = "Electronics", condition =0.0.
        '''
        super().__init__(category = "Electronics", condition = condition )

    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "A gadget full of buttons and secrets."
