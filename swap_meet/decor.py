from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = 0, age = None):
        super().__init__(condition = condition, age = age, category = "Decor")

    def __str__(self):
        return "Something to decorate your space."
    
    def condition_description(self):
        return super().condition_description()
    
    def age_description(self):
        return super().age_description()