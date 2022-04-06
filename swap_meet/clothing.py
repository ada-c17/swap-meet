from swap_meet.item import Item


class Clothing(Item):
    
    category = "Clothing"
    
    def __init__(self, *args, **kwargs):
        super().__init__(category=Clothing.category, *args, **kwargs) 

    @staticmethod
    def __str__():
        return "The finest clothing you could wear."
