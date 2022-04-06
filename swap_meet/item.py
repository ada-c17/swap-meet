class Item:
     '''
    Class that represents an item.
    
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

    def __init__(self, category = "", condition = 0.0 ):
        '''
        Constructs attributes for Item object, default values: category = empty string, condition = 0.0.
        '''
        self.category = category
        self.condition = condition

    def __str__(self):
        '''
        Overrides Python default __str__ method and returns "Hello World!"
        '''
        return "Hello World!"

    def condition_description(self):
        if 0 <= self.condition < 1: 
            return "You don't want to touch this with a 10 foot pole!"
        elif self.condition < 2:
            return "You should wash your hands after handling this."
        elif self.condition < 3: 
            return "It's not great, but if you want it..."
        elif self.condition < 4:
            return "That's not a bad option!"
        elif self.condition <= 5:
            return  "What a steal! Wrap it up, and let's go!"

