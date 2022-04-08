
from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition 
        
    def __str__(self):
        item ="Hello World!"
        return item

    def condition_description(self):
        if self.condition == 0:
            return "About to fall to pieces."
        elif self.condition == 1: 
            return "This is a fixer-upper."
        elif self.condition == 2: 
            return "Needs a little bit of love."
        elif self.condition == 3:
            return "It works, but has been well loved."
        elif self.condition == 4: 
            return "Good condition"
        elif self.condition == 5:
            return "Pristine, impeccable, immaculate!!!" 
    