# wave 5
# inherit from item class
# add condition attribute
from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, category="Clothing", condition=0):
        super().__init__(category, condition)
        # self.category = category
    
    def __str__(self):
        return "The finest clothing you could wear."