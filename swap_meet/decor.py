from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, condition = 0):
        self.category = "Decor"
        self.condition = condition
    
    def __str__(self):
        super().__str__()
        return "Something to decorate your space."