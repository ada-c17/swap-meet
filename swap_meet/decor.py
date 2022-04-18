from swap_meet.item import Item
from datetime import date
class Decor(Item):
    def __init__(self,  condition=0, age =date(2020,1,1)):
        super().__init__("Decor", condition, age)

    def __str__(self):
        return "Something to decorate your space."