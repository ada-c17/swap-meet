class Item:
    def __init__(self, category = None, condition = 0.0):
        if category is None:
            category = ""
        self.category = category
        self.condition = condition    


    '''Return name of category in the terminal, when instance is assign'''
    def __repr__(self):
        return self.category


    '''Return string "Hello World!" if category is not defined'''
    def __str__(self):
        return "Hello World!"


    '''Method assigning specific string-output depends of condition'''
    def condition_description(self):
        if 0 < self.condition <= 1:
            condition_description = "Poor"
        elif 1 < self.condition <= 2:
            condition_description = "Fair"
        elif 2 < self.condition <= 3:
            condition_description = "Good"
        elif 3 < self.condition <= 4:
            condition_description = "Like New"
        elif 4 < self.condition <= 5:
            condition_description = "New"
        return condition_description              
