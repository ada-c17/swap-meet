from .item import Item

class Electronics(Item):

    def __init__(self, condition=None):
        self.category  = "Electronics"
        self.condition = condition
        self.message = "A gadget full of buttons and secrets."

