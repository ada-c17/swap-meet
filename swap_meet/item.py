QUALITY_DESCRIPTIONS = {
    0: "Probably best to scrap for parts",
    1: "Fixer-Upper",
    2: "Fine.",
    3: "Used, still has lots of life",
    4: "Gently used; gave-up-on-this-hobby tier",
    5: "Waited too long to return this; new in box"
}

class Item:

    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        rating_bound = int(self.condition)
        return QUALITY_DESCRIPTIONS[rating_bound]