class Item:
    
    # constructor for class Item
    def __init__(self, category = None, condition = None):
        if category == None:
            category = ""
        if condition == None:
            condition = 0
        self.category = category
        self.condition = condition

    # method to stringify an Item
    def __str__(self):
        return "Hello World!"

    # method to describe condition in words based on value
    def condition_description(self):
        self.yikes = 0
        self.eh = 1
        self.alright = 2
        self.dude = 3
        self.sweet = 4
        self.goldjerrygold = 5