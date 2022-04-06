from .item import Item

class Decor(Item):
    # def __init__(self, category = "Decor", condition = 3.5, age = 2):
    #     self.category = category
    #     self.condition = condition
    #     self.age = age
    def __init__(self, category = "Decor", condition = 3.5, **age):
        super().__init__(**age) #age inherited as and set as keyword argument in Item
        self.category = category
        self.condition = condition 

    def __str__(self):
        return "Something to decorate your space."
