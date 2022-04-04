class Electronics:
    def __init__(self, category="Electronics", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."

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
