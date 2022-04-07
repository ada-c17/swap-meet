class Item:
    def __init__(self, category="", condition=0, age=0): # str are immutable, so okay to use as default parameter
        self.category = category
        self.condition = condition
        self.age = age 
    
    def __str__(self): 
        return "Hello World!" 

    def condition_description(self):
        if self.condition <= 0:
            return "Stay away - it ain't worth it."
        elif self.condition >= 1 and self.condition < 2:
            return "You might need some holy water to cleanse it."
        elif self.condition >= 2 and self.condition < 3:
            return "It's not bad, but it's not good either."
        elif self.condition >= 3 and self.condition < 4:
            return "Not too shabby."
        elif self.condition >= 4 and self.condition < 5:
            return "Basically brand-new."
        elif self.condition == 5:
            return "Treat yo self!"