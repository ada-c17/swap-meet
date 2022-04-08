from swap_meet.item import Item
class Electronics(Item):
    '''
        An Electronics-type Item: a gadget full of buttons and secrets.
        
        Attributes:
            category (str): item type
            condition (float): item quality (range 0-5; default 0.0)
    '''
    def __init__(self, category = "Electronics", condition=0.0):
        super().__init__(category, condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
    
