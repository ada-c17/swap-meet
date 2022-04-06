class Item:
    def __init__(self, category=None, condition=0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    