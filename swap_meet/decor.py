from swap_meet.item import Item
'''
Decor class is a child of the Item class, imported above. 
Differences from parent include unique __str__ method and category attribute hard-coded to "Decor".
'''


class Decor(Item):
    def __init__(self, condition=0, age=None):
        super().__init__(category="Decor", condition=condition, age=age)

    def __str__(self):
        return "Something to decorate your space."
