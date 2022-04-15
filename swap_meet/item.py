class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_chart = {
            0: "This item has been heavily used.",
            1: "This item has been moderately used.",
            2: "This item has been partially used.",
            3: "This item is in good condition.",
            4: "This item is in great condition.",
            5: "This item is brand new"
        }

        return condition_chart[self.condition]