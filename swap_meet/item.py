from nis import cat

class Item:
    def __init__(self, category="", condition = 0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 4 < self.condition <= 5:
            self.condition_desc = "Perfect Condition!"
        elif 3 < self.condition <= 4:
            self.condition_desc = "Decent Condition"
        elif 2 < self.condition <= 3:
            self.condition_desc = "OK Condition"
        elif 1 < self.condition <= 2:
            self.condition_desc = "Eh Condition"
        elif 0 < self.condition <= 1:
            self.condition_desc = "Poor Condition"
        return self.condition_desc


    
