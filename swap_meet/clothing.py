from swap_meet.item import Item
from datetime import date
class Clothing(Item):
    def __init__(self, condition=0, age =date(2020,1,1)):
        super().__init__("Clothing", condition, age)
    
    def __str__(self):
        return "The finest clothing you could wear."
