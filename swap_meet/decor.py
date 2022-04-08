from.item import Item

class Decor(Item):
    def __init__(self, age = 0, category = "Decor", condition = 0):
        super().__init__(age, category = category, condition = condition)

    def __str__(self):
        return "Something to decorate your space."