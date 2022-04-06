# wave 5
# inherit from item class
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, category="Electronics"):
        super().__init__(category)
        # self.category = category
    
    def __str__(self):
        return "A gadget full of buttons and secrets."