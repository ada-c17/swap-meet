#from swap_meet.vendor import Vendor

class Item:
    def __init__(self,category=""):
        #super().__init__(inventory)
        self.category=category

    def __str__(self):
        return (f"Hello World!")   

