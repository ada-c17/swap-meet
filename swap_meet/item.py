
class Item:
    def __init__(self, condition = 0, category = ""):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"


    def condition_description(self):
        if self.condition == 0:
            return "Absolute trash"
        elif self.condition == 1:
            return "A real fixer-upper"
        elif self.condition == 2:
            return "I guess it could be worse"
        elif self.condition == 3:
            return "Now we're getting somewhere"
        elif self.condition == 4:
            return "Pretty darn good"
        elif self.condition == 5:
            return "Absolute perfection"

    



