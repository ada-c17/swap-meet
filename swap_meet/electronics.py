from .item import Item
class Electronics(Item):
    def __init__(self,category= None, condition = 0):
        if category is None:
            category = ""
        self.category = "Electronics"
        if condition is 0:
            condition = 0
        self.condition = condition 
    def __str__(self):
        return "A gadget full of buttons and secrets."
