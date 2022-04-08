from swap_meet.item import Item

class Clothing(Item):
    def __init__(self,category = "Clothing", condition = 0.0):
        super().__init__(category = "Clothing",condition = condition)

    def __str__(self):
        stringfied_item = "The finest clothing you could wear."
        return str(stringfied_item)

    
    
    