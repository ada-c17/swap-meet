class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    
    def condition_description(self):
        if self.condition == 0.0:
            return "You might want some gloves"
        elif self.condition <= 2 or self.condition < 2.0:
            return "Not the best!"
        elif self.condition <= 4 or self.condition < 4.0:
            return "It sort of looks okay"
        else:
            return "mint"
