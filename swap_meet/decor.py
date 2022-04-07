from swap_meet.item import Item
#wave 5
class Decor(Item):
    def __init__(self, category="Decor", condition=0.0): #can change
        super().__init__(category, condition) #no overwritten

    def __str__(self):
        #return f"{super().__str__()} Something to decorate your space."
        return "Something to decorate your space."

    
    def condition_description(self):
        return super().condition_description()