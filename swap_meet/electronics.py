from .item import Item

class Electronics(Item):
    def __init__(self, condition = 0.0):
        '''
        Constructs attributes for Electronics object from parent class, default values: category = "Electronics", condition =0.
        '''
        super().__init__(condition = condition, category = "Electronics")


    def __str__(self):
        '''
        Overrides parent str method and returns message.
        '''
        return "A gadget full of buttons and secrets."
