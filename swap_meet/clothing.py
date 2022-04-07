from .item import Item


class Clothing(Item):
    
    category = "Clothing"
    
    def __init__(self, condition=0, age=None):
        super().__init__(type(self).category, condition, age)

    @staticmethod
    def __str__():
        return "The finest clothing you could wear."
