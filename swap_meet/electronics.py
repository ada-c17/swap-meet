from swap_meet.item import Item

class Electronics(Item):
    """
    A class to represent an Electronics item.

    """

    def __init__(self, condition=0.0):
        super().__init__(category = "Electronics", condition=condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
