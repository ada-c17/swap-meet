from swap_meet.item import Item

class Decor(Item):
    """
    A child class of Item to hold decor object data.

    ...
    Attributes
    ----------
    category: str
        category of item that defaults to "Decor"
    condition: float
        describes condition of item from a range of 0-5
    age: float
        describes how old an object is by year
    """

    def __init__(self, condition=0, age=0):
        super().__init__("Decor", condition, age)

    def __str__(self):
        return "Something to decorate your space."
