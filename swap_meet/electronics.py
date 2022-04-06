from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=0):
        super().__init__(category="Electronics", condition=condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
