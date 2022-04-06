from .item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 3.5, age = 2):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "The finest clothing you could wear."
