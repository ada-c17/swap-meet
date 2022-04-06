from swap_meet.item import Item
class Decor(Item):
    """Child class that inherits attributes and methods from Item class as parent class:"""


    def __init__(self, condition = None):
        """Setting category as default with "Decor" which inherits attributes from Item class."""
        super().__init__(category= "Decor", condition = condition)
        


    def __str__(self):
        """Overriding method from Item class by returning differenct value in string format if condition is empty."""
        if not self.condition:
            return "Something to decorate your space."


    