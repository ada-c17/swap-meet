class Item:
    """
    A class to represent an item.

    Attributes
    ----------
    category : str
        string representing the item category

    Methods
    -------
    __str__:
        overrides str() method to return "Hello World!"
    """
    
    def __init__(self, category="", condition=0.0):
        """ Constructs all the necessary attributes for the item object. """
        self.category = category
        self.condition = condition
    
    def __str__(self):
        """ Overrides string method. Returns "Hello World!" """
        return "Hello World!"
    
    def condition_description(self):
        """ Returns a description based on the score of the instance's condition. """
        if self.condition == 0:
            return "This is a hot mess. Run!"
        elif self.condition == 1:
            return "Barely worth the money."
        elif self.condition == 2:
            return "Somewhat decent."
        elif self.condition == 3:
            return "Not too shabby"
        elif self.condition == 4:
            return "This is some good stuff!"
        elif self.condition == 5:
            return "Beyonce herself would want this!"