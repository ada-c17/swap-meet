class Item:
    def __init__(self, category=None, condition=0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        CONDITION_RATING = {
            1: "parts only",
            2: "play condition",
            3: "good used condition",
            4: "excellent used condition",
            5: "like new condition"
        }

        condition = CONDITION_RATING[self.condition]
        return condition