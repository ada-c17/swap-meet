from swap_meet.item import Item
class Decor(Item):
    '''
        A Decor-type Item: something to decorate your space.

        Attributes:
            category (str): item type
            condition (float): item quality (range 0-5; default 0.0)
    '''
    def __init__(self, category="Decor", condition=0.0):
        super().__init__(category, condition)
    
    def __str__(self):
        return "Something to decorate your space."
    