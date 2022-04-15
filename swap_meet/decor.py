from swap_meet.item import Item

class Decor(Item):

    def __init__(self, condition = 0):
        super().__init__(condition = condition, category = "Decor")
        self.condition = condition


    def __str__(self):
        self = "Something to decorate your space."
        return f"{self}"