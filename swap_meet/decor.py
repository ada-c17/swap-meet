from .item import Item

class Decor(Item):
    '''A class that represents items at the meet used to brighten up spaces.
    
    Attributes
    ----------
    category : str
        represents the type of the item, 'Decor' unless directly updated

    condition : float
        represents the condition of the item
    '''
    
    def __init__(self, condition = 10.0):
        '''Creates an instance of the Decor class.
        
        Parameters
        ----------
        condition : float
            represents condition of the item, defaults to 10.0 (new) if absent
        '''

        super().__init__(category = 'Decor', condition = condition)

    def __str__(self):
        return "Something to decorate your space."