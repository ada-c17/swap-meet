from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, condition=0.0, age=0):
        super().__init__(condition, age, category="Electronics")

    def __str__(self):
        return "A gadget full of buttons and secrets."
