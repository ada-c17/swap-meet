from sre_constants import CATEGORY
from unicodedata import category




class Item:
    def __init__(self, category = None):
        if not category:
            self.category = ""
        else:
            self.category = category

    def __str__(self):
        return "Hello World!"
