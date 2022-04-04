class Item:
    
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 0.5:
            return "This is trash."
        elif 0.5 <= self.condition < 1.5:
            return "Poor"
        elif 1.5 <= self.condition < 2.5:
            return "Fair"
        elif 2.5 <= self.condition < 3.5:
            return "Good"
        elif 3.5 <= self.condition < 4.5:
            return "Really Good"
        elif self.condition >= 4.5:
            return "Mint"