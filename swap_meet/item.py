class Item:
    def __init__(self,category='',condition=None):
        self.category = category
        if condition:
            self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        return str(self.condition)