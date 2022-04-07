from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0, age = None):
        super().__init__(condition = condition, age = age, category = "Clothing")

    def __str__(self):
        return "The finest clothing you could wear."
    
    def condition_description(self):
        return super().condition_description()

    def age_description(self):
        return super().age_description()