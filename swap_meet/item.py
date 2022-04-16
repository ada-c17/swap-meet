class Item:
    def __init__(self, category = "", condition = 0, age = 0):
        
        self.category = category
        self.condition = condition
        self.age = age
        

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 1.0:
            return "Heavily used"
        elif self.condition <= 2.0:
            return "Used"
        elif self.condition <= 3.0:
            return "Acceptable"
        elif self.condition <= 4.0:
            return "Very good"
        elif self.condition <= 5.0:
            return "Brand new"
        





