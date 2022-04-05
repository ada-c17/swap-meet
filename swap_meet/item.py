class Item:
    
    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        # age is optional parameter to not affect original tests
        # age if given, is an integer to represent how long vendor has owned it
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        # how should this handle floats?
        descriptions = {
            1: "Don't buy it",
            2: "At your own risk",
            3: "Meh",
            4: "Near perfect",
            5: "Never been used"
        }
        return descriptions[self.condition]