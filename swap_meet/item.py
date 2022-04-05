class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        descriptors = [
            "Mint",
            "Like New",
            "Gently Used",
            "Used",
            "Well Used",
            "Bad Condition",
        ]

        if 1 > self.condition >= 0:
            return descriptors[0]
        elif 2 > self.condition >= 1:
            return descriptors[1]
        elif 3 > self.condition >= 2:
            return descriptors[2]
        elif 4 > self.condition >= 3:
            return descriptors[3]
        elif 5 > self.condition >= 4:
            return descriptors[4]
        elif self.condition == 5:
            return descriptors[5]