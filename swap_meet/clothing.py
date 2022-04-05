from .item import Item

class Clothing(Item):
    def __init__(self, condition=0, category="Clothing"):
        super().__init__(condition)
        self.category = category
    
    def __str__(self):
        return "The finest clothing you could wear."
    
    