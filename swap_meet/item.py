class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition


    def __str__(self):
        return "Hello World!"


    def condition_description(self):
        descriptions = ["Destroyed",
                        "Barely there",
                        "Heavily used",
                        "Good",
                        "Mint",
                        "New"]
        
        return descriptions[self.condition]
