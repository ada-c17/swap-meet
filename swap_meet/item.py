class Item:
    
    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "Mint"
        elif self.condition >= 4:
            return "Really Good"
        elif self.condition >= 3:
            return "Good"
        elif self.condition >= 2:
            return "Fair"
        elif self.condition > 0:
            return "Poor"
        else:
            return "The condition has not been accurately assesed."