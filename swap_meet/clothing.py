from swap_meet.item import Item

class Clothing(Item):
    def __init__(self,category = "Clothing", condition = 0.0 ):
        super().__init__(category = "Clothing",condition = condition )
        # if not category:
        #     category= ""
        # self.category = str(category)
        # self.condition = condition

    def __str__(self):
        stringfied_item = "The finest clothing you could wear."
        Item = stringfied_item
        Item = str(Item)
        return str(stringfied_item)

    
    
    