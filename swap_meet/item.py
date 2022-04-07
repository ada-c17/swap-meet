class Item:
    def __init__(self,category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Poor"
        if self.condition == 1:
            return "Fair"
        if self.condition == 2:
            return "Good"
        if self.condition == 3:
            return "Very good"
        if self.condition == 4:
            return "Like new"
        if self.condition ==5:
            return "New"