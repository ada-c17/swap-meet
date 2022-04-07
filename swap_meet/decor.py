from swap_meet.item import Item

class Decor(Item):

    def __init__(self, condition = "", age = 0):
        self.category = "Decor"
        self.condition = condition
        self.age = age

        
    # stringify method for Decor
    def __str__(self):
        return "Something to decorate your space."