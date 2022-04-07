from swap_meet.item import Item

class Decor(Item):
    """
    A child class of Item to hold decor object data.

    ...
    Attributes
    ----------
    category: str
        category of item that defaults to "Electronics"
    """

    def __init__(self, condition=0):
        super().__init__("Decor", condition)

    def __str__(self):
        return "Something to decorate your space."
