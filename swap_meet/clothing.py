from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0):
        self.category = "Clothing"
        self.condition = condition
        # Would using super() here be more efficient? Why does the code below not work?
        # super().__init__(condition=0)
    def __str__(self):
        return "The finest clothing you could wear."