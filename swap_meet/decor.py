from .item import Item

class Decor(Item):
    def __init__(self,**kwargs):
        kwargs['category'] = 'Decor'
        super().__init__(**kwargs)

    def __str__(self):
        return "Something to decorate your space."