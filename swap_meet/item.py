
class Item:
    def __init__(self, category = "" , condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "This item should not be for sale but whatever."
        elif self.condition == 1:
            return "This item has seen better days. Still functional though."
        elif self.condition == 2:
            return "This is fairly used but decent."
        elif self.condition == 3:
            return "This is in good condition."
        elif self.condition == 4:
            return "This item is nearly new!"
        elif self.condition == 5:
            return "This item is brand new and never used."