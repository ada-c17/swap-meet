

class Item:
    def __init__(self, condition=0, category=""):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 0 and self.condition <= 1:
            return "very poor"
        elif self.condition > 1 and self.condition <= 2:
            return "poor"
        elif self.condition > 2 and self.condition <= 3:
            return "medium"
        elif self.condition > 3 and self.condition  <= 4:
            return "good"
        elif self.condition > 4 and self.condition <= 5:
            return "mint"
