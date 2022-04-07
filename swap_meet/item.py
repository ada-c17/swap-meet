class Item:
    def __init__(self,category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Distressed"
        if self.condition == 1:
            return "Used fair"
        if self.condition == 2:
            return "Used good"
        if self.condition == 3:
            return "Used very good"
        if self.condition == 4:
            return "Used like new"
        if self.condition ==5:
            return "New"