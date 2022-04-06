class Item:
    def __init__(self, category = None, condition = 0.0):
        if category == None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition

    def __str__(self):
        self.category = "Hello World!" 
        return self.category

    def condition_description(self):
        if self.condition > 4.0 and self.condition <= 5.0:
            return "Great condition"
        elif self.condition > 3.0 and self.condition <= 4.0:
            return "Very Good condition"
        elif self.condition > 2.0 and self.condition <= 3.0:
            return "Good condition"
        elif self.condition > 1.0 and self.condition <= 2.0:
            return "Fair condition"
        elif self.condition >= 0.0 and self.condition <= 1.0:
            return "Poor condition"



    

