from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 0, age = 1.0):
        # Question - here in this super(),__init__, do I need to specify category is clothing e.g.
        # category = "Clothing" OR because it's already stated in line 4 in the __init__ for Clothing,
        # it doesn't need to be explicitly set again?
        super().__init__(category, condition, age)

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        return Item.condition_description(self)