class Decor:
    def __init__(self, category = "Decor", condition = 0):
        self.condition = condition
        self.category = category

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        if self.condition == 0.0:
            return "Poor"
        elif self.condition == 1.0:
            return "Acceptable"
        elif self.condition == 2.0:
            return "Good" 
        elif self.condition == 3.0:
            return "Very Good" 
        elif self.condition == 4.0:
            return "Like New" 
        elif self.condition == 5.0:
            return "Brand New" 