class Electronics:
    def __init__(self, category="Electronics", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

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
