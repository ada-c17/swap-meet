class Item:
    
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"    

    def condition_description(self):
        if self.condition == 5:
            return "mint"
        elif self.condition >= 4:
            return "lightly used"
        elif self.condition >= 3:
            return "some wear and tear"
        elif self.condition >= 2:
            return "moderate damage"
        elif self.condition >= 1:
            return "significant damage"
        return "better off not touching it."    