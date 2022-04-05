from swap_meet.item import Item

class Decor:
    def __init__(self, condition):
        self.category = "Decor"
        self.condition = condition
    def __str__(self):
        return "Something to decorate your space."
