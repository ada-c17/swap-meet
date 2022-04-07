class Item:
    '''
    Item class that is a base class/ parent class that has condition descriptions for items.
    '''

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def condition_description(self):
        '''
        Return different conditions depending on argument inputted. Default condition is set to 0.
        '''
        if self.condition == 0:
            return "This is brand new!"
        elif self.condition >= 1 and self.condition <= 3:
            return "This is gently used!"
        elif self.condition > 3:
            return "This is heavily used!" 
    
    def __str__(self):
        '''
        Returns this string when printing this class.
        '''
        return "Hello World!"