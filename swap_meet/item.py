class Item:

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 5:
            return "This is brand new"
        if self.condition == 4:
            return "This is mint condition"
        if self.condition == 3:
            return "Has wear commiserate of age"
        if self.condition == 2:
            return "Almost time to retire"
        if self.condition ==1:
            return "About to fall apart"
        if self.condition == 0:
            return "Disintegrate"
    