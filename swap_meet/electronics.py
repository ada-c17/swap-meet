from swap_meet.item import Item
'''
Electronics is a child class of Item. It is a type of Item (ElectronicsItem).
Its attribute category has a namesake string value.
'''

class Electronics(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Electronics", condition = condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
