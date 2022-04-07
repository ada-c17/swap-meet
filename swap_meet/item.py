class Item:
    def __init__(self, category="", condition=0.0):
        """category is an empty string by default"""
        self.category = category
        self.condition = condition
        
    #wave 3
    def __str__(self):
        """overrides class object's __str__ method"""
        #return f"{type(self).__name__} Hello World!"
        return "Hello World!"
    
    def condition_description(self):
        if self.condition in range(0,3):
            return f"Condition: {self.condition} is poor."
        elif self.condition in range(3,5):
            return f"Condition: {self.condition} is average."
        elif self.condition == 5:
            return f"Condition: {self.condition} is super."
    
    