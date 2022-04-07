# from swap_meet.vendor import Vendor


from ast import Str


class Item():

    def __init__(self, category = ""):
        self.category = category
        self.message = "Hello World!"

    def __str__(self):
        return self.message

    def condition_description(self):
        if self.condition < 5:
            return "Not as great as it could be :("
        else: 
            return "WOWZERS"