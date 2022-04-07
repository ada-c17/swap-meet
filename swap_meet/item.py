class Item:
    '''
    A class to represent an item.
    Parent class for clothing, decor and electronics classes.
    Attributes:
        category: string
        condition: number
    Methids: __str__, condition_description
    '''

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 3:
            return 'heavily used'
        elif 3 <= self.condition <= 5:
            return "mint"