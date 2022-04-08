class Item:
    CONDITION_DESCRIPTIONS = {0:"Poor", 1: "Okay", 2: "Fair", 3: "Good", 4: "Excellent", 5: "Pristine"}

    def __init__(self, category = "", condition = 0.0):
        self.category = category

        if condition < 0 or condition > 5: #check that condition is between 0 and 5
            raise ValueError
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        return Item.CONDITION_DESCRIPTIONS[int(self.condition)]