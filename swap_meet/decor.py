from swap_meet.item import Item
class Decor(Item):

    category = "Decor"

    def __init__(self, condition=0):
        super().__init__(Decor.category, condition)

    @staticmethod
    def __str__():
        return "Something to decorate your space."