class Item:
    def __init__(self, category="", condition=0.0, age=0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        description = ""
        if 4.5 < self.condition <= 5.0:
            description = "EXCELLENT"
        elif 4.0 < self.condition <= 4.5:
            description = "VERY GOOD"
        elif 3.0 < self.condition <= 4.0:
            description = "GOOD"
        elif 2.0 < self.condition <= 3.0:
            description = "FAIR"
        elif 1.0 < self.condition <= 2.0:
            description = "POOR"
        else:
            description = "VERY POOR"
        return f"The condition of this item is {description}"