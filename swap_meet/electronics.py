from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, condition = "", age = 0):
        self.category = "Electronics"
        self.condition = condition
        self.age = age


    # stringify method for Electronics
    def __str__(self):
        return "A gadget full of buttons and secrets."