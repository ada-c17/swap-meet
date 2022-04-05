class Item:

    CONDITION_RATINGS = {
    0: "You can help me throw in the trash",
    1: "Poor",
    2: "Fair",
    3: "Good Condition",
    4: "Mint",
    5: "Brand New"
    }

    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    @staticmethod
    def __str__():
        return "Hello World!"
    
    def condition_description(self):
        return Item.CONDITION_RATINGS.get(self.condition, None)