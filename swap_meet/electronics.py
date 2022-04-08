from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition = 0.0):
        self.category = category
        self.condition = float(condition)

    def __str__(self):
        return f'A gadget full of buttons and secrets.'
