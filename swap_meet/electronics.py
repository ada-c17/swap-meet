from swap_meet.item import Item


class Electronics(Item):
    
    def __init__(self, condition = 0, age = None):
        self.category = "Electronics"
        self.condition = condition
        self.age = age

    #override str() for Electronics, returns "A gadget full of buttons and secrets."
    def __str__(self):
        return "A gadget full of buttons and secrets."
