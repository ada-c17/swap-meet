# wave 5
# inherit from item class
# add condition attribute
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, category="Electronics", condition=0):
        super().__init__(category, condition)
        # self.category = category
    
    def __str__(self):
        return "A gadget full of buttons and secrets."