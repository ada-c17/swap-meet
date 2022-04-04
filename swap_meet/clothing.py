from unicodedata import category
from swap_meet.item import Item
class Clothing(Item):
    
    category = "Clothing"
    
    def __init__(self, condition=0):
        super().__init__(Clothing.category, condition)

    @staticmethod
    def __str__():
        return "The finest clothing you could wear."
