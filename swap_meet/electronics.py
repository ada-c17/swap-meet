from .item import Item

class Electronics(Item):
    # def __init__(self, category = "Electronics", condition = 3.5, age = 2):
    #     self.category = category
    #     self.condition = condition
    #     self.age = age
    def __init__(self, category = "Electronics", condition = 3.5, **age):
        super().__init__(**age) #age inherited as and set as keyword argument in Item
        self.category = category
        self.condition = condition 
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

