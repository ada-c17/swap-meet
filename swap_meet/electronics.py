from swap_meet.item import Item
'''
Electronics class is a child of the Item class, imported above. 
Differences from parent include unique __str__ method and category attribute hard-coded to "Electronics".
'''


class Electronics(Item):
    def __init__(self, condition=0, age=None):
        super().__init__(category="Electronics", condition=condition, age=age)

    def __str__(self):
        return "A gadget full of buttons and secrets."
