from swap_meet.item import Item

class Electronics(Item):
    """
    A class to represent an electronics item. Inherits attributes and methods from Item class. 
    
    ...
    Inherited Attributes:

    condition : int or float
        an optional attribute describing the condition of the item, defaulting to 0. higher numbers indicate better condition.
    age: int or float
        an optional attribute describing how many years old an item is, defaulting to None. cannot be negative.
    category: str
        a attribute describing the category of the item, set to Electronics
    
    ...
    Inherited Methods:

    condition_description():
        Returns string describing the condition of the item
    
    age_description():
        Returns string describing item's age
    
    ...
    Methods:

    __str__:
        represents class objects as a string.

    """
    
    def __init__(self, condition = 0, age = None):
        super().__init__(condition = condition, age = age, category = "Electronics")

    def __str__(self):
        return "A gadget full of buttons and secrets."

