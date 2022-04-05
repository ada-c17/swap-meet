class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "You gotta see it to beleive it"
        elif self.condition == 1:
            return "A hand-me-down many, many times over"
        elif self.condition == 2:
            return "Like reliving your college dorm"
        elif self.condition == 3:
            return "A gift from my ex - he was ok"
        elif self.condition == 4:
            return "Like new - not new but like it"
        elif self.condition == 5:
            return "The Beyonce of objects"
