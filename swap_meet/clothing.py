from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, condition = 0):
        super().__init__(condition = condition, category = "Clothing")
        self.condition = condition
        
        
        
    def __str__(self):
        self = "The finest clothing you could wear."
        return f"{self}"

