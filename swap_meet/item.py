# from swap_meet.vendor import Vendor

class Item:
    # create category parameters, where deafalt is empty string
    def __init__(self, category = None):
        if category is None:
            category = ""
        self.category = category      

    # return string, when instance is assign
    def __repr__(self):
        return self.category

# item_a = Item(category="clothing")
# print(item_a)