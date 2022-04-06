from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, condition=0, category="Clothing", age=0):
        self.condition = condition
        self.category = category
        self.age = age
    def __str__(self):
        return "The finest clothing you could wear."

