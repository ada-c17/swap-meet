#from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None, category = None):
        # why do we specify that it's a list as a default param?
        if not inventory:
           inventory = []
        self.inventory = inventory
        self.category = category


    def add(self, item):
        if not item:
            return False

        self.inventory.append(item)
        return item

    def remove(self, item):
        #inventory_copy = self.inventory.deepcopy
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        self.list_of_items_per_cat = []

        for item in self.inventory:
            if item.category == category:
                self.list_of_items_per_cat.append(item)

        print(self.list_of_items_per_cat)

        return self.list_of_items_per_cat




'''
Notes and Questions:


# inventory = ["ball", "jeans" "shirt"]
# # inventory = ["clothing", "decor", "electronics"] #<--
# inventory[0] = ["jeans", "shirt"]


# print(Vendor.get_by_category("instruments"))

# questions
# what is the orange thing on top of vendor (does it equal class)?
# and now what is the purple thing (instance method)


'''

