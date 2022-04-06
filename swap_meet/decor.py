# wave 5
# inherit from item class
from swap_meet.item import Item
class Decor(Item):
    def __init__(self, category="Decor"):
        super().__init__(category)
        # self.category = category
    
    def __str__(self):
        return "Something to decorate your space."