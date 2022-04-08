from .item import Item

class Electronics(Item):
    '''A class that represents gadgets available to be swapped at the meet.

    Attributes
    ----------
    category : str
        represents the type of the item, 'Electronics' unless directly updated

    condition : float
        represents the condition of the item
    '''
    
    def __init__(self, condition = 10.0):
        '''Creates an instance of the Electronics class.
        
        Parameters
        ----------
        condition : float
            represents condition of the item, defaults to 10.0 (new) if absent
        '''
        super().__init__(category = 'Electronics', condition = condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
