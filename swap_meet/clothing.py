from swap_meet.item import Item

class Clothing(Item):
    """
    A child class of Item to hold clothing object data.

    ...
    Attributes
    ----------
    category: str
        category of item that defaults to "Clothing"
    condition: float
        describes condition of item from a range of 0-5
    """

    def __init__(self, condition=0):
        super().__init__("Clothing", condition)


    def __str__(self):
        return "The finest clothing you could wear."
