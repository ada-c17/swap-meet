class Clothing:
    def __init__(self, category="Clothing", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

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