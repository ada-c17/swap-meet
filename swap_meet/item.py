class Item:
    def __init__(self, age = 0, category = "", condition = 0):
        # ??? dont need to do following bc str is unmutable? 
        # self.category = category if category else ""
        
        self.category = category
        self.condition = condition
        self.age = age
    

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_description = {
            5: "Never used",
            4: "Like new",
            3: "Good condition",
            2: "Old but srill has its function",
            1: "Missing parts",
            0: "Blind box!!!",
        }
        
        for key, value in condition_description.items():
            if key == self.condition:
                return value