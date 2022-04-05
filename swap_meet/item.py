class Item:
    def __init__(self, category = ""):
        '''
        Constructs attributes for Item object, default category value is empty string.
        '''
        self.category = category

    def __str__(self):
        '''
        Overrides Python default __str__ method and returns "Hello World!"
        '''
        return "Hello World!"

