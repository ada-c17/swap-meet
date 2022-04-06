class Item:

    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = condition #add check that condition is within 0 and 5

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        CONDITION_DESCRIPTIONS = {0:"Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
        return CONDITION_DESCRIPTIONS[int(self.condition)]