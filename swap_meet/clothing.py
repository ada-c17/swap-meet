from swap_meet.item import Item

class Clothing(Item):
    """A child class of Item, representing aspects of an Item specific to Clothing"""
    def __init__(self, category="Clothing", condition=0.0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "The finest clothing you could wear."
