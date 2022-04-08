from swap_meet.item import Item
class Electronics(Item):
    """Child class that inherits attributes and methods from Item class as parent class:"""
    

    def __init__(self, condition = 0, age = 0):
        """Setting category attribute as default with "Electronics" and inherits attributes from Item class."""
        super().__init__(category= "Electronics", condition = condition, age = age)


    def __str__(self):
        """Printing the returnning message string when printing instance of Electronics class."""
        return "A gadget full of buttons and secrets."

    



    
