from swap_meet.item import Item


class Clothing(Item):
    def __init__(self,category ='', condition = 0):
        super().__init__(category = "Clothing", condition = condition)
    def __str__(self, category = "Clothing"):  
        category = "The finest clothing you could wear."
        return category

