from .item import Item

class Electronics(Item):
    def __init__(self, condition = 0, age = 0): #if these attributes already found in parent, only call here when user needs to have option to update them
        super().__init__(category = "Electronics", condition = condition, age = age) #category is hard coded here because it will not be updated in the Electronics class
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

