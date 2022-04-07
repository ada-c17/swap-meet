from swap_meet.item import Item

class Electronics(Item):
    def __init__(self,category = "Electronics", condition = 0.0):
        super().__init__(category = "Electronics",condition = condition)
        # if not category:
        #     category= ""
        # self.category = str(category)
        # self.condition = condition

    def __str__(self):
        stringfied_item = ('A gadget full of buttons and secrets.')
        Item = stringfied_item
        Item = str(Item)
        return str(stringfied_item)
    
    