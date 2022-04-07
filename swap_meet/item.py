# from swap_meet.vendor import Vendor


from ast import Str


class Item():

    def __init__(self, category = ""):
        self.category = category
        self.message = "Hello World!"

    def __str__(self):
        '''
        Returns individual message unique to each subclass of Item.
        '''
        return self.message

    def condition_description(self):
        '''
        Returns a description based on the condition of the item in question.
        '''

        if self.condition < 5:
            return "Not as great as it could be :("
        else: 
            return "WOWZERS"