#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, anyString="Hello World!", category = ""):
        self.category = category
        self.y = anyString
    # def __str__()

    def __str__(self):
        return str(self.y)

# item1 = Item()
# print(str(item1))


