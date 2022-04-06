class Item:
    def __init__ (self, category=str(), condition = 0):
        self.category = category 
        self.condition = condition

    def __str__ (self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "This would be better served on a pedestal in a museum"
        elif self.condition == 1:
            return "I mean...It works, mostly"
        elif self.condition == 2:
            return "This is...acceptable"
        elif self.condition == 3:
            return "Passable for sure"
        elif self.condition == 4:
            return "Lightly used, a couple scuffs, but still in good shape!"
        elif self.condition == 5:
            return "Like new!"



