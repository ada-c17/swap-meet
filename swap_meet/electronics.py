from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, age=0, condition=0, category="Electronics"):
        super().__init__(age, condition, category)

    def __str__(self):
        return "A gadget full of buttons and secrets."
