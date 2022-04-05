# from .vendor import Vendor

class Item:
  
    def __init__(self,category = ""):
        self.category = category

    def __str__(self):
        return "Hello World!"

    # def swap_items():

my_item = Item()
their_item = Item()
