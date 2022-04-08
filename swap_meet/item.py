class Item:
    
    # constructor for class Item
    def __init__(self, category = ""):
        self.category = category
        self.condition = 0
        self.age = 0

    # method to stringify an Item
    def __str__(self):
        return "Hello World!"

    # method to describe condition in words based on value
    def condition_description(self):
        conditions = {
            0 : "yikes",
            1 : "eh",
            2 : "not bad",
            3 : "nice",
            4 : "sweet",
            5 : "amazing"
        }
        return conditions[self.condition]

    # method to describe age in words based on value
    def age_description(self):
        age = {
            0 : "brand new",
            1 : "fresh",
            2 : "classic",
            3 : "last season's",
            4 : "retro",
            5 : "ancient",
        }
        return age[self.age]