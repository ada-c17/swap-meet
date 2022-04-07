from swap_meet.item import Item
class Clothing(Item):
    """Child class that inherits attributes and methods from Item class as parent class:"""


    def __init__(self, condition = None, age = None):
        """Setting category attribute as default with "Clothing" and inherits attributes from Item class."""
        super().__init__(category= "Clothing", condition = condition, age = age)
        

    def __str__(self):
        """Printing the returnning message string when printing instance of Clothing class."""
        
        return "The finest clothing you could wear."

    