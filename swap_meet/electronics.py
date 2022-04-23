from swap_meet.item import Item

class Electronics(Item):
    # def __init__(self, category = "Electronics", condition = 0, age = 1.0):
    def __init__(self, condition = 0, age = 1.0):

        super().__init__(category = "Electronics", condition=condition, age=age)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    # def condition_description(self):
    #     return Item.condition_description(self)