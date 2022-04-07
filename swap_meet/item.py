from pydoc import describe


class Item:
    def __init__(self, condition = 0, category = ""):
        self.condition = condition
        self.category = category

    def __str__(self): 
        return "Hello World!"
    
    def condition_description(self):
        if 0 <= self.condition < 1:
            self.description = "Heavily used"
            return self.description
        elif 1 <= self.condition < 3:
            self.description = "Moderately used"
            return self.description
        elif 3 <= self.condition < 4:
            self.description = "Good condition"
            return self.description
        elif 4 <= self.condition <= 5:
            self.description = "Great condition"
            return self.description