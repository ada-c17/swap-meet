class Vendor:
    # wave 1
    # attributes: 
    #   inventory - an empty list
    # instance methods:
    #   add - takes in one item and adds to inventory, returns item added
    #   remove - takes in one item and removes from inventory, returns item removed

    # wave 2
    # add instance method:
    #   get_by_category - takes in one string item and returns list of inventory items in the same category

    # wave 3
        # add instance method:
        # swap_items
            # args: Vendor, Item(my_item), Item(their_item)
            # removes my_item from vendor's inventory and adds to friend's inventory
            # removes their_item from friend's inventory and adds to vendor inventory
            # returns True
            # returns False if my_item not in Vendor's inventory or their_item not in freind's inventory

    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        same_category_items = []
        for item in self.inventory:
            if item.category == category:
                same_category_items.append(item)
        return same_category_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True