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
            print(Item.CONDITIONS[int(self.age)])
            return Item.CONDITIONS[int(self.age)]
        except:
            return "Condition must be a whole number between 0 and 5."
        # if self.condition == 0.0:
        #     return "Poor"
        # elif self.condition == 1.0:
        #     return "Acceptable"
        # elif self.condition == 2.0:
        #     return "Good" 
        # elif self.condition == 3.0:
        #     return "Very Good" 
        # elif self.condition == 4.0:
        #     return "Like New" 
        # elif self.condition == 5.0:
        #     return "Brand New" 
        # else: 
        #     return "Condition must be a whole number between 1 and 5."