class Item:
    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        description = {
            0: "new", 
            1: "barely used",
            2: "good for a couple of days",
            3: "found it in Paris",
            4: "light blue color",
            5: "has weird smell"
            }
        return description[self.condition]