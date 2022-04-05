class Item:
    def __init__(self, condition=0.0, age=0, category=""):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 5:
            return "Like new"
        elif self.condition == 4:
            return "Very good"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 2:
            return "Acceptable"
        elif self.condition == 1:
            return "Ugly"
        elif self.condition == 0:
            return "As is"
    
