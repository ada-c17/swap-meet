# wave 5
# inherit from item class
from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, category="Clothing"):
        super().__init__(category)
        # self.category = category
    
    def __str__(self):
        return "The finest clothing you could wear."