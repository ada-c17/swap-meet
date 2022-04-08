from swap_meet.item import Item

class Electronics(Item):
    """A child class of Item, representing aspects of an Item specific to Electronics"""   
    
    def __init__(self, category="Electronics", condition=0.0, age=None):
        self.category = category
        self.condition = condition
        self. age = age 

    def __str__(self):
        return "A gadget full of buttons and secrets."
