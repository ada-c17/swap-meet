from swap_meet.item import Item


class Decor(Item):
    

    def __init__(self, condition = 0, age = None):
        self.category = "Decor"
        self.condition = condition
        self.age = age
    
    #override str() for Decor, returns "Something to decorate your space."
    def __str__(self):
        return "Something to decorate your space."