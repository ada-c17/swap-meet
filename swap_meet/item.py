class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return ("New")
        if self.condition == 1:
            return ("Used like new")
        if self.condition == 2:
            return ("Used")
        if self.condition == 3:
            return ("Fair")
        if self.condition == 4:
            return ("Dont buy it")
        if self.condition == 5:
            return("Run") 
