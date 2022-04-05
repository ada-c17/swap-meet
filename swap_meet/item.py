from nis import cat


class Item:
    def __init__(self,category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__ (self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            self.condition = "Poor"
        elif self.condition == 1:
            self.condition = "Could be better"
        elif self.condition == 2:
            self.condition = "So so"
        elif self.condition == 3:
            self.condition = "Quite good"
        elif self.condition == 4:
            self.condition = "Good"
        else:
            self.condition = "Excellent"
        return self.condition


