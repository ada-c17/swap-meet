from swap_meet.item import Item
'''
Clothing is a child class of Item. It is a type of Item (ClothingItem).
Its attribute category has a namesake string value.
'''

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Clothing", condition = condition)

    def __str__(self):
        return "The finest clothing you could wear."