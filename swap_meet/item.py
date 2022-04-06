class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if not self.condition:
            return "This item has been heavily used."
        elif self.condition == 1:
            return "This item has been moderately used."
        elif self.condition == 2:
            return "This item has been partially used."
        elif self.condition == 3:
            return "This item is in good condition."
        elif self.condition == 4:
            return "This item is in great condtion."
        elif self.condition == 5:
            return "This item is brand new!"