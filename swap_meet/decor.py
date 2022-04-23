from swap_meet.item import Item

class Decor(Item):
    # def __init__(self, category = "Decor", condition = 0, age = 1.0): # deleted this based on feedback
    def __init__(self, condition = 0, age = 1.0):

        super().__init__(category = "Decor", condition=condition, age=age)

    def __str__(self):
        return "Something to decorate your space."

    # Not needed since it's the same as in the parent, so no override needed
    # def condition_description(self):
    #     return Item.condition_description(self)