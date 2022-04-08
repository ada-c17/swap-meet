# from .vendor import Vendor

class Item:
  
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if condition == 5:
            return "best"

 

my_item = Item()
their_item = Item()
