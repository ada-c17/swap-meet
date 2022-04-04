class Clothing:
    def __init__(self, condition=0):
        self.category = "Clothing"
        self.condition = condition
    def __str__(self):
        return "The finest clothing you could wear."
    
    def condition_description(self):
        if self.condition == 0:
            condition_desc = "pls no"
        elif self.condition == 1:
            condition_desc = "heavily used"
        elif self.condition == 2:
            condition_desc = "fair"
        elif self.condition == 3:
            condition_desc = "very good"
        elif self.condition == 4:
            condition_desc = "like new"
        elif self.condition == 5:
            condition_desc = "mint"
        return condition_desc