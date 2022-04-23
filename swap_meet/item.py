class Item:
    """
    A class to represent an item.

    ...
    Attributes:

    condition : int or float, optional
        attribute describing the condition of the item, defaulting to 0. higher numbers indicate better condition.
    age: int or float, optional
        attribute describing how many years old an item is, defaulting to None. cannot be negative.
    category: str, optional
        attribute to describe the kind of item, defaulting to an empty string.
    
    ...
    Methods:

    __str__:
        represents class objects as a string.
    
    condition_description():
        Returns string describing the condition of the item
    
    age_description():
        Returns string describing item's age

    """
    
    def __init__(self, condition = 0, age = None, category = ""):
        self.condition = condition
        self.category = category
        if age and age < 0:
            raise ValueError("Age may not be a negative number")
        self.age = age


    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        """Returns string describing the condition of the item"""

        if self.condition <= 1:
            return "I mean I wouldn't touch this with a ten foot pole but, uh, you do you."
        elif self.condition <= 2:
            return "It's....tolerable. I suppose. If one must."
        elif self.condition <= 3:
            return "Decent."
        elif self.condition <= 4:
            return "Alright, NOW we're talking. Nothing's perfect, right?"
        elif self.condition <= 5:
            return "Excellent. Full marks. Drinks all around!"
        else:
            return "Oh my god BUY THIS NOW ITS CONDITION IS OUT OF THIS WORLD"
    
    def age_description(self):
        """Returns string describing item's age"""

        if self.age is None:
            return "The age of this item is unknown. Please judge it by its condition."
        elif self.age == 0:
            return "This item is brand new."
        elif self.age < 1:
            return "This item is less than 1 year old."
        elif self.age == 1:
            return "This item is 1 year old."
        else:
            return f"This item is {self.age} years old."

