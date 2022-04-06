from swap_meet.item import Item
class Clothing(Item):
    """Child class that inherits attributes and methods from Item class as parent class:"""


    def __init__(self, **kwargs):
        """Overridig the category attribute from Item class by setting default"""
        super().__init__(**kwargs)
        self.category = "Clothing"


    def __str__(self):
        """Overriding method from Item class by returning differenct value in string format if condition is empty."""
        if not self.condition:
            return "The finest clothing you could wear."

    