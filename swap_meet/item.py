class Item:
    category = ""
    condition = 0
    
    def __init__(self, **kwargs):
        if 'category' in kwargs:
            self.category = kwargs['category']
        
        if 'condition' in kwargs:
            self.condition = kwargs['condition']    
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        return str(self.condition)