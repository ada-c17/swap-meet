from swap_meet.item import Item
class Electronics(Item):
    """Child class that inherits attributes and methods from Item class as parent class:"""
    
    # Wave 5
    def __init__(self, category = "Electronics", **kargs):
        """Inheriting all attributs from Item class"""
        super().__init__(category = "Electronics", **kargs)


    def __str__(self):
        """Returning value in string format by override inherited method from Item class."""
        return str("A gadget full of buttons and secrets.")


    def condition_description(self):
        """Returing inherited method from Item class."""
        return super().condition_description()
