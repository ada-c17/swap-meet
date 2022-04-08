from swap_meet.item import Item

class Decor(Item):
    def __init__(self,category = "Decor", condition = 0.0):
        super().__init__(category = "Decor",condition = condition)
        if not category:
            category= ""
        self.category = str(category)
        self.condition = condition

    def __str__(self):
        stringfied_item = "Something to decorate your space."
        return str(stringfied_item)

    