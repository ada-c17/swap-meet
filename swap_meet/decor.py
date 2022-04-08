from swap_meet.item import Item

class Decor(Item):
    '''Decor class is instantiated and inherits from Item class'''

    def __init__(self, category = "Decor", condition = 0, age = 0):
        super(). __init__(category, condition, age)

    def __str__(self):
        return "Something to decorate your space."
