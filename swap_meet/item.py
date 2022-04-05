class Item:
    
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_dict = {
            1: "Don't buy it",
            2: "At your own risk",
            3: "Meh",
            4: "Near perfect",
            5: "Never been used"
        }
        return condition_dict[self.condition]