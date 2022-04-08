from swap_meet.item import Item

class Decor(Item):
    """A child class of Item, representing aspects of an Item specific to Decor"""   
    def __init__(self, category="Decor", condition=0.0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Something to decorate your space."
