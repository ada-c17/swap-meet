from swap_meet.item import Item
from datetime import date
class Electronics(Item):
    def __init__(self, condition=0, age =date(2020,1,1)):
        super().__init__("Electronics", condition, age)

    def __str__(self):
        return "A gadget full of buttons and secrets."
