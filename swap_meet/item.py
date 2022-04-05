class Item:
    
    def __init__(self, category=None, condition=None):
        if not category:
            category = ""
        self.category = category
        if not condition:
            condition = 0
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
        #return f"{self.category}"

    def condition_description(self):
        if self.condition < 1:
            return "ewww"
        elif self.condition < 2:
            return "umm"
        elif self.condition < 3:
            return "eh"
        elif self.condition < 4:
            return "good"
        elif self.condition < 5:
            return "great"
        elif self.condition >= 5:
            return "perfect"
