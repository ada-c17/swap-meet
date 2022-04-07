
class Item:
    
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "New"
        elif self.condition == 4:
            return "Like New"
        elif self.condition == 3:
            return "So So"
        elif self.condition == 2:
            return "Just ok"
        else:
            self.condition > 0 and self.condition < 1
            return "return it"
