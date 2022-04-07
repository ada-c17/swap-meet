from swap_meet.item import Item

class Decor(Item):
    def __init__(self, age=0, condition=0, category="Decor"):
        super().__init__(age, condition, category)

    def __str__(self):
        return "Something to decorate your space."