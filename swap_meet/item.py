class Item:
    def __init__(self, category = ""):
        self.category = category
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Distressed"
        elif self.condition == 1:
            return "Used fair"
        elif self.condition == 2:
            return "Used good"
        elif self.condition == 3:
            return "Used very good"
        elif self.condition == 4:
            return "Used like new"
        elif self.condition == 5:
            return "New"
            



