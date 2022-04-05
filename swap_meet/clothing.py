from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 0, age = 1.0):
        super().__init__(category, condition, age)

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        return Item.condition_description(self)