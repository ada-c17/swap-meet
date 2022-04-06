from swap_meet.item import Item
'''
Clothing class is a child of the Item class, imported above. 
Differences from parent include unique __str__ method and category attribute hard-coded to "Clothing".
'''


class Clothing(Item):
    def __init__(self, condition=0, age=None):
        super().__init__(category="Clothing", condition=condition, age=age)

    def __str__(self):
        return "The finest clothing you could wear."
