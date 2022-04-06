class Item:
    def __init__(self, category = "", condition = 0):
        '''
        Constructs attributes for Item object, default values: category = empty string, condition =0.
        '''
        self.category = category
        self.condition = condition

    def __str__(self):
        '''
        Overrides Python default __str__ method and returns "Hello World!"
        '''
        return "Hello World!"

    def condition_description(self, condition_description):
        self.condition_description = condition_description

