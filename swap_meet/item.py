#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 2:
            return "Quite used but super cute and could refactor it like bad code"
        elif 2 <= self.condition <= 3:
            return "Very used but quality fabric and fit"
        elif 3 <= self.condition <= 4:
            return "Not bad"
        elif 4 <= self.condition <= 4.5:
            return "Mint condition, sparkly and all"
        elif 4.5 <= self.condition <= 4.9:
            return "Never worn, like new"
        elif self.condition == 5:
            return "Label still on, never worn, like new"



# item1 = Item()
# item1.condition = 3.5
# print(item1.condition_description())

