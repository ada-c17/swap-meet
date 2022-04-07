from swap_meet.item import Item

class Electronics(Item):
    """
    A child class of Item to hold electronics object data.

    ...
    Attributes
    ----------
    category: str
        category of item that defaults to "Electronics"
    """

    def __init__(self, condition=0):
        super().__init__("Electronics", condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
