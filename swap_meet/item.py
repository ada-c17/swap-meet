class Item:
    
    '''Item class is instantiated'''
    def __init__(self, category=None, condition = 0, age = 0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        '''Function returns condition description based on quantitative value assigned to condition'''
        
        if self.condition == 0:
            return f"terrible"
        if self.condition == 1:
            return f"not great"
        if self.condition == 2:
            return f"kinda ok"
        if self.condition == 3:
            return f"you'll do"
        if self.condition == 4:
            return f"basic"
        if self.condition == 5:
            return f"vibe"