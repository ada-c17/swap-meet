from swap_meet.item import Item
class Clothing(Item):
    '''
        A Clothing-type Item: the finest clothing you could wear.
        
        Attributes:
            category (str): item type
            condition (float): item quality (range 0-5; default 0.0)
    '''
    def __init__(self, category="Clothing", condition=0.0):
        super().__init__(category, condition)

    def __str__(self):
        return "The finest clothing you could wear."