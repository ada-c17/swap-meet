from .item import Item

class Clothing(Item):
    def __init__(self,**kwargs):
        kwargs['category'] = 'Clothing'
        super().__init__(**kwargs)

    def __str__(self):
        return "The finest clothing you could wear."