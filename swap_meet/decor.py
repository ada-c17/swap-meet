from .item import Item


class Decor(Item):
    def __init__(self, condition=0, category="Decor"):
        super().__init__(condition)
        self.category = category

    def __str__(self):
        return "Something to decorate your space."
