

class Item:
    
    def __init__(self, category = "", condition = 0, age = None):
        self.category = category
        self.condition = condition
        self.age = age

    #override str() for Item, returns "Hello World!" instead
    def __str__(self):
        return "Hello World!"


    #describes condition based on the value, range from 0 to 5
    def condition_description(self):

        if self.condition == 0:
            return "Terrible condition"
        
        if self.condition == 1:
            return "Bad condition"

        if self.condition == 2:
            return "Slightly bad condition"

        if self.condition == 3:
            return "Acceptable condition"

        if self.condition == 4:
            return "Good condition"

        if self.condition == 5:
            return "Mint conditon"


