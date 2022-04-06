from swap_meet.item import Item


class Decor(Item):

    category = "Decor"

    def __init__(self, *args, **kwargs):
        super().__init__(category=Decor.category, *args, **kwargs)  

    @staticmethod
    def __str__():
        return "Something to decorate your space."