# from swap_meet.vendor import Vendor

class Item:
    # create category parameters, where deafalt is empty string
    def __init__(self, category = None):
        if category is None:
            category = ""
        self.category = category