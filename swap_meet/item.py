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
    
    def __init__(self, category=""):
        """ Constructs all the necessary attributes for the item object. """
        self.category = category
    
    def __str__(self):
        """ Overrides string method. Returns "Hello World!" """
        return "Hello World!"