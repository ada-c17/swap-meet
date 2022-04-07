class Item:
    CONDITIONS = {
        0: "Poor",
        1: "Acceptable",
        2: "Good",
        3: "Very Good",
        4: "Like New",
        5: "Brand New"
    }

    def __init__(self, category = "", condition = 0, age = 1.0):
        self.category = category 
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        try:
            return Item.CONDITIONS[self.condition]
        except:
            return "Condition must be a float between 0 and 5."