
class Item:
    def __init__(self, category="", condition=0, age= float("inf")):
        self.category = category
        self.condition = condition 
        self.age = age


    def __str__(self):
        return "Hello World!"
    
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