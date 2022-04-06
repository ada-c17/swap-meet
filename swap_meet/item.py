class Item:

    def __init__(self, condition = 0.0, age = 0.0,category= None):
        if category == None:
            category = ""
        self.category = category
        if condition == 0.0:
            condition = 0.0
        self.condition = condition
        if age is 0.0:
            age = 0.0
        self.age = age

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0.0:
            return "Heavily used"
        elif self.condition == 1.0:
            return "Very Bad"
        elif self.condition == 2.0:
            return "Bad"
        elif self.condition == 3.0:
            return "Average"
        elif self.condition == 4.0:
            return "Used like new"  
        elif self.condition == 5.0:
            return "Never used"
            

        





