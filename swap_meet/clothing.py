from .item import Item

class Clothing(Item):

    def __init__(self, condition=None):
        self.category = "Clothing"
        self.condition = condition
        self.message = "The finest clothing you could wear."



