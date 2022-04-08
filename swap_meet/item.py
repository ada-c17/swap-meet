class Item:
    def __init__(self, category = "", condition = 0, age = 1.0):
        self.category = category 
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    # I liked this below solution for condition_description() and 
    # how it has fewer lines of code, but the one I kept seems more flexible
    # as you can handle something like 3.5 whereas the below solution requires
    # a whole number between 0 and 5 or it would raise a KeyError.

    # CONDITIONS = {
    #     0: "Poor",
    #     1: "Acceptable",
    #     2: "Good",
    #     3: "Very Good",
    #     4: "Like New",
    #     5: "Brand New"
    # }

    # def condition_description(self):
    #     try:
    #         return Item.CONDITIONS[self.condition]
    #     except:
    #         return "Condition must be a float between 0 and 5."

    def condition_description(self):
            if self.condition == 5.0:
                return "Brand New" 
            if self.condition >= 4.0 and self.condition < 5.0:
                return "Like New"
            elif self.condition >= 3.0 and self.condition < 4.0:
                return "Very Good"
            elif self.condition >= 2.0 and self.condition < 3.0:
                return "Good" 
            elif self.condition >= 1.0 and self.condition < 2.0:
                return "Acceptable" 
            elif self.condition >= 0.0 and self.condition < 1.0:
                return "Poor" 
            else: 
                return "Condition must be a float between 0 and 5."
