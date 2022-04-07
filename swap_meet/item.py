class Item:
    """
    A class to hold item object data.

    ...
    Attributes
    ----------
    category: str
        category of an item
    """

    def __init__(self, category=""):
        self.category = category

    def __str__(self):
        return "Hello World!"
