class Item:
    '''A class that represents items available to be swapped by vendors at the meet.
    
    Instances can optionally specify a category and a condition for the item. 
    '''

    def __init__(self, category = '', condition = None):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        return str(self.condition)