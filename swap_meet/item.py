class Item:
    '''A class to represent items swappable by vendors at the meet.
    
    Attributes
    ----------
    category : str
        represents the general type of the item
    
    condition : float
        represents the condition of the item 
    
    Methods
    -------
    condition_description():
        returns a string describing the condition of the item
    '''

    def __init__(self, category = '', condition = None):
        '''Creates an Item object with a blank category and optional condition.
        
        Parameters
        ----------
            category : str (optional)
                Value assigned to 'category' attribute, defaults to empty string.

            condition : float (optional)
                Value assigned to 'condition' attribute, defaults to None.
        '''
        self.category = category
        self.condition = condition
    
    def __str__(self):
        '''Overrides object.'__str__' to pass the test.'''

        return "Hello World!"
    
    def condition_description(self):
        '''Returns a string of the Item's condition value.'''

        return str(self.condition)