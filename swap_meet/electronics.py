from .item import Item


class Electronics(Item):
    def __init__(self, condition=0, category="Electronics"):
        super().__init__(condition, category)

    def __str__(self):
        return "A gadget full of buttons and secrets."
