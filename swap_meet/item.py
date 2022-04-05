class Item:
    def __init__(self, condition = 0, category=""):
        self.condition = float(condition)
        self.category = category
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 2: 
            return f"Poor condition: {round(self.condition, 1)}"
        elif self.condition <= 3:
            return f"Good used condition: {round(self.condition, 1)}"
        elif self.condition <= 4:
            return f"Excellent used condition: {round(self.condition, 1)}"
        else:
            return f"Like-new condition: {round(self.condition, 1)}"