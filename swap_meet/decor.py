from swap_meet.item import Item
'''
Decor is a child class of Item. It is a type of Item (DecorItem).
Its attribute category has a namesake string value.
'''

class Decor(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Decor", condition = condition)

    def __str__(self):
        return "Something to decorate your space."



