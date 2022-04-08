class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__ (self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 1: 
            return "BAD. Buy at your own risk"

        elif self.condition < 2: 
            return "Not the worst. Not the best"
        
        elif self.condition < 3: 
            return "Decent!"
        
        elif self.condition < 4: 
            return "Pretty good"
        
        elif self.condition <= 5: 
            return "Good"
        
        else:
            return "Try again!"
    
    

