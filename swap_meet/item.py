class Item:
    """
    A class to represent a Item.
    
    '''
    Attributes
    ----------
    category(str): a category of an item, default is an empty string.
    condition(int): a condition rating of an item, default set to 0.

    Methods
    -------
    condition_description():
        Describes an item's condition based on the rating.
    
    """
    def __init__(self, category="", condition=0):
        """
        Constructs all the necessary attributes for the Item object.

        Parameters
        ----------
        category(str): a category of an item, default is an empty string.
        condition(int): a condition rating of an item, default set to 0.
        """
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """
        Describes an item's condition based on the rating.

        Returns
        -------
        Description (str) based on the condition.
        """

        if self.condition < 1.0: 
            return "Not even a trash goblin wants this."
        elif self.condition < 2.0:
            return "You are not that desperate." 
        elif self.condition < 3.0:
            return "Could be better."
        elif self.condition < 4.0:
            return "Not bad."
        elif self.condition < 5.0:
            return "Does this spark joy?"
        elif self.condition == 5.0:
            return "Legendary Purple Grade."

