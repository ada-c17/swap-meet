from swap_meet.item import Item

class Electronics(Item):
    '''Electronics class is instantiated and inherits from Item class'''

    def __init__(self, category = "Electronics", condition = 0, age = 0):
        super(). __init__(category, condition, age)

    def __str__(self):
        return "A gadget full of buttons and secrets."
