class Item:
    def __init__(self, condition=0, category="", age = 0):
        self.condition = condition
        self.category = category
        self.age = age
    #stringify item
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Yikes, this one has been through a lot. Keep looking!"
        elif self.condition == 1:
            return "Well, it you can't find anything else."
        elif self.condition == 2:
            return "Some wear and tear"
        elif self.condition == 3:
            return "Used"
        elif self.condition == 4:
            return "Like new"
        elif self.condition == 5:
            return "Brand new!"
