from .item import Item

class Clothing(Item):
    
    def __init__(self, condition=0, age=0):
        super().__init__(condition=condition, age=age, category="Clothing")

    def __str__(self):
        return "The finest clothing you could wear."