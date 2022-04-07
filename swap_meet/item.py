

class Item:
    
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        #self.age = age

    #override str() for Item, returns "Hello World!" instead
    def __str__(self):
        return "Hello World!"


    #describes condition based on the value, range from 0 to 5
    def condition_description(self):

        if self.condition == 0:
            return "Wash your hands with bleach after purchase"
        
        if self.condition == 1:
            return "Wash your hands with soap after purchase"

        if self.condition == 2:
            return "Kind of gross"

        if self.condition == 3:
            return "Acceptably gross"

        if self.condition == 4:
            return "Not gross at all"

        if self.condition == 5:
            return "Mint conditon"


