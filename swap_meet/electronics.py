from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, category = None, condition = None):
        category = "Electronics"
        self.category = category
        self.condition = condition

    # stringify method for Electronics
    def __str__(self):
        return "A gadget full of buttons and secrets."