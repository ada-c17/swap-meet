class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition > 5:
            return "That's probably an item."

        condition_descriptions = {0: "Yep, that's an item.",
        1: "Previously owned", 2: "Previously despised",
        3: "Previously tolerated", 4: "Previously enjoyed",
        5: "Previously loved"}

        return condition_descriptions[self.condition]

