from swap_meet.item import Item
class Decor(Item):
    """Child class that inherits attributes and methods from Item class as parent class:"""

    # Wave 5
    def __init__(self, category = "Decor", **kargs):
        """Inheriting all attributs from Item class"""
        super().__init__(category = "Decor", **kargs)


    def __str__(self):
        """Returning value in string format by override inherited method from Item class."""
        return str("Something to decorate your space.")


    def condition_description(self):
        """Returing inherited method from Item class."""
        return super().condition_description()