class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        description = ""
        if self.condition == 0:
            description = "EXCELLENT"
        elif self.condition == 1:
            description = "VERY GOOD"
        elif self.condition == 2:
            description = "GOOD"
        elif self.condition == 3:
            description = "FAIR"
        else:
            description = "POOR"
        return f"The condition of this item is {description}"