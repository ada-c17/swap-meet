from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, age=0, condition=0, category="Clothing"):
        super().__init__(age, condition, category)

    def __str__(self):
        return "The finest clothing you could wear."