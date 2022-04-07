from unicodedata import category


class Item:
    def __init__(self,category = "", condition = None, age = None):
        self.category = category
        self.condition = condition
        self.age = age
        
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0 :
            return "Red"
        elif self.condition == 1 :
            return "Brown"
        elif self.condition == 2: 
            return "Orange"
        elif self.condition == 3 :
            return "Yellow"
        elif self.condition == 4 : 
            return "Blue"
        elif self.condition == 5 :
            return "Green"
        