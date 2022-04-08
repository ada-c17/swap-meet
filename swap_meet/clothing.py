from .item import Item

class Clothing(Item):
    '''
    Class representing a clothing item to be traded
    Child of Item class

    Methods:
        condition_description() from Item class

    Variables:
        category: category of clothing default is Clothing
        condition: condition of an item from 0-5
    '''
    def __init__(self, category="Clothing", condition=0):
        super().__init__(category, condition)

    def __str__(self):
        return "The finest clothing you could wear."
