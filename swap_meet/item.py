class Item:
    
    def __init__(self, category=str(), condition=0, age=0): #using empty string constructor to explicitly note string data type expected
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "barely sellable"
        elif self.condition == 1:
            return "heavily used"
        elif self.condition == 2:
            return "meh"
        elif self.condition == 3:
            return "reasonable"
        elif self.condition == 4:
            return "good"
        elif self.condition == 5:
            return "mint"