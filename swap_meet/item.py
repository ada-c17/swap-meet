from nis import cat


class Item:
    def __init__(self,category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__ (self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Poor"
        elif self.condition == 1:
            return "Could be better"
        elif self.condition == 2:
            return "So so"
        elif self.condition == 3:
            return "Quite good"
        elif self.condition == 4:
            return "Good"
        else:
            return "Excellent"
            


