class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def __repr__(self):
        return self.category

    def condition_description(self):
        if self.condition > 5:
            return "Nothing is perfect. Please enter a condition value between 1 and 5"
        elif self.condition == 5:
            return "As close to perfect as it gets."
        elif self.condition >= 4:
            return "Nothing a bit of spit polish won't fix."
        elif self.condition >= 3:
            return "In the biz, we call that 'Well-Loved.'"
        elif self.condition >= 2:
            return "Maybe try Target?"
        elif self.condition >=1:
            return "Handle with caution... and a Geiger counter."
        elif self.condition >= 0:
            return "This product is as real as that Nigerian prince I funded..."
        else:
            return False