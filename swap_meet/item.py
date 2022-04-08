class Item:
    def __init__(self, category = "", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_description = {
            0: "Very Poor",
            1: "Poor",
            2: "Fair",
            3: "Good",
            4: "Excellent",
            5: "Mint"   
        }

        condition = condition_description[self.condition]

        return condition

