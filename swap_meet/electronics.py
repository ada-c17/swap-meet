from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, condition = 0):
        super().__init__(condition = condition, category = "Electronics")
        self.condition = condition

    def __str__(self):
        self = "A gadget full of buttons and secrets."
        return f"{self}"
