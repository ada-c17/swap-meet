from swap_meet.item import Item

class Electronics:
    def __init__(self, condition):
        self.category = "Electronics"
        self.condition = condition
    def __str__(self):
        return "A gadget full of buttons and secrets."
