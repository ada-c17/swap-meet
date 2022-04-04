from .item import Item

class Electronics(Item):
    def __init__(self,**kwargs):
        kwargs['category'] = 'Electronics'
        super().__init__(**kwargs)

    def __str__(self):
        return "A gadget full of buttons and secrets."
