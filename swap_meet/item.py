import math

class Item:
    
    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        # age is optional parameter to not affect original tests
        # age if given, is an integer to represent how long (yrs) vendor has owned it
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        # handle values not between 1 and 5 and floats
        adj_condition = self.condition
        if self.condition > 5: 
            adj_condition = 5
        elif self.condition < 1:
            adj_condition = 1
        else:
            adj_condition = math.floor(self.condition + 0.5)

        descriptions = {
            1: "Don't buy it",
            2: "At your own risk",
            3: "Meh",
            4: "Near perfect",
            5: "Never been used"
        }
        return descriptions[adj_condition]