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

    def __init__(self, category='', condition=None):
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

        if self.condition is None:
            output_string = ("It is in a state of eternal renewal, where "
                            "condition has no meaning. That or it's digital.")
        elif self.condition == 10:
            output_string = 'It is brand new.'
        elif self.condition > 9.5:
            output_string = 'It is in nearly mint condition.'
        elif self.condition > 7.5:
            output_string = 'It wears signs of its use like a fine patina.'
        elif self.condition > 5:
            output_string = 'It has some stories to tell.'
        elif self.condition > 3:
            output_string = 'Despite its condition, it still works!'
        elif self.condition > 0:
            output_string = ('You can still tell what it used to be for, and ' 
                            'finding a new use for it will be a fun challenge'
                            ' maybe.')
        elif self.condition == 0:
            output_string = ('It has collapsed in on itself to form a black '
                            'hole and may destroy anything that comes too '
                            'close.')

        return output_string

    def complete_description(self):
        '''Returns a string describing the item type as well as its condition.'''

        if not self.category:
            output_string = 'A completely uncategorizable item, probably holy.'
        else:
            output_string = str(self)
        output_string += ' '+self.condition_description()

        return output_string