from swap_meet.item import Item

class Electronics(Item):
    
    def __init__(self, condition=None):
        self.category = "Electronics"
        if not condition:
            condition = 0
        self.condition = condition
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
