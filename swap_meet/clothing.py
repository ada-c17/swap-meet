class Clothing:
    def __init__(self, category="Clothing", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "The finest clothing you could wear."

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