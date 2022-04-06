class Item:
    def __init__(self, category=None, condition=None):
        if not category:
            category = ""
        self.category = category
        
        if not condition:
            condition = 0
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"