from .item import Item

class Clothing(Item):
    '''A class to represent wearable items available to be swapped at the meet.
    
    Attributes
    ----------
    category : str
        represents the type of the item, 'Clothing' unless directly updated

    condition : float
        represents the condition of the item
    '''

    def __init__(self, condition = 10.0):
        '''Creates an instance of the Clothing class.
        
        Parameters
        ----------
        condition : float
            represents condition of the item, defaults to 10.0 (new) if absent
        '''

        super().__init__(category = 'Clothing', condition = condition)

    def __str__(self):
        return "The finest clothing you could wear."