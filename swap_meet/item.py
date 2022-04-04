'''
In Wave 2 we will create the Item class and the get_by_category method.

There is a module (file) named item.py inside of the swap_meet package (folder)

Inside this module, there is a class named Item

Each Item will have an attribute named category, which is an empty string by default

When we initialize an instance of Item, we can optionally pass in a string with the keyword argument category

Instances of Vendor have an instance method named get_by_category

It takes one argument: a string, representing a category
This method returns a list of Items in the inventory with that category

'''
from swap_meet.vendor import Vendor

class Item():
    def __init__(self, category = ""):
        self.category = category

# item =

