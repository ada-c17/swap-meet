from .item import Item

class Electronics(Item):
    def __init__(self, category="Electronics", condition=0):#unsure of if the redundant value sets are necessary
        super().__init__(category, condition)
        
    def __str__(self):
        return "A gadget full of buttons and secrets."

