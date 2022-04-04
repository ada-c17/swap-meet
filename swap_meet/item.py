class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category 
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self, condition):
        if condition == 0.0:
            return "Poor"
        elif condition == 1.0:
            return "Acceptable"
        elif condition == 2.0:
            return "Good" 
        elif condition == 3.0:
            return "Very Good" 
        elif condition == 4.0:
            return "Like New" 
        elif condition == 5.0:
            return "Brand New" 