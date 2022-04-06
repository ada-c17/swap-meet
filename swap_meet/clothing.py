from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 0):
        super().__init__(category, condition) # new line

    def __str__(self):
        return "The finest clothing you could wear."



'''
A better name for Clothing would have been ClothingItem.
Which HAS a category Clothing.
Clothing is a class, and it is a Child of class Item. Item is the Parent class.
'''

cloth = Clothing()
print(cloth.category)
print(str(cloth))
# cloth.condition = 4.8
print(cloth.condition)