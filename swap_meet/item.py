class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        description = ""
        if self.condition == 5.0:
            description = "EXCELLENT"
        elif self.condition == 4.0:
            description = "VERY GOOD"
        elif self.condition == 3.0:
            description = "GOOD"
        elif self.condition == 2.0:
            description = "FAIR"
        elif self.condition == 1.0:
            description = "POOR"
        else:
            description = "VERY POOR"
        return f"The condition of this item is {description}"