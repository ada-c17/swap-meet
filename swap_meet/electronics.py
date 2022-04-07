from .item import Item
class Electronics(Item):
    def __init__(self, condition=0, age=0):
        Item.__init__(self, category="Electronics", condition=condition, age = age)
        
    def __str__(self):
        return "A gadget full of buttons and secrets."