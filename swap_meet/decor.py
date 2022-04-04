class Decor:
    def __init__(self, category="Decor", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        CONDITIONS = {
            0: "Mint",
            1: "Okay",
            2: "Good",
            3: "Great",
            4: "Excellent",
            5: "Flawless"
        }
        return CONDITIONS[self.condition]