from .item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition = 0.0):
        '''
        Constructs attributes for Electronics object, default values: category = "Electronics", condition =0.
        '''
        self.category = category
        self.condition = condition

    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "A gadget full of buttons and secrets."
