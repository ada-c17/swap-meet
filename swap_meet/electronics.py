from.item import Item

class Electronics(Item):
    def __init__(self, age = 0, category = "Electronics", condition = 0):
        super().__init__(age, category = category, condition = condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
