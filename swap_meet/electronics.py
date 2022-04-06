from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, condition=0, category ="Electronics", age=0):
        self.condition = condition
        self.category = category
        self.age = age
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
