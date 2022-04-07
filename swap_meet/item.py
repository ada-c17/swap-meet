class Item:
    def __init__(self, category = "", condition = 0):
        
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 1.0:
            return "Heavily used"
        elif self.condition < 2.5:
            return "Used"
        elif self.condition < 3.5:
            return "Acceptable"
        elif self.condition < 4.5:
            return "Very good"
        elif self.condition < 4.9:
            return "Like new"
        else:
            return "Brand new"






