class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "heavily used"
        if self.condition in range(1, 2):
            return "signs of wear"
        if self.condition in range(2, 3):
            return "lightly used"
        if self.condition in range(3, 4):
            return "nearly new"
        if self.condition in range(4, 5):
            return "almost flawless"
        if self.condition == 5:
            return "mint!"
