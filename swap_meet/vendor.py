class Vendor:
    # wave 1
    # attributes: 
    #   inventory - an empty list
    # instance methods:
    #   add - takes in one item and adds to inventory, returns item added
    #   remove - takes in one item and removes from inventory, returns item removed

    def __init__(self, inventory=None):
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    # wave 2
    # add instance method:
    #   get_by_category - takes in one string item and returns list of inventory items in the same category

    def get_by_category(self, category):
        same_category_items = []
        for item in self.inventory:
            if item.category == category:
                same_category_items.append(item)
        return same_category_items

    # wave 3
    # add instance method:
    # swap_items
        # args: Vendor, Item(my_item), Item(their_item)
        # removes my_item from vendor's inventory and adds to friend's inventory
        # removes their_item from friend's inventory and adds to vendor inventory
        # returns True
        # returns False if my_item not in Vendor's inventory or their_item not in freind's inventory

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
    
    # wave 4
    # add instance method:
    # swap_first_item
        # arg: another vendor
        # removes first item from self inventory and adds friend's 1st item
        # removes friend's first item from friend inventory and adds self first item
        # returns True
        # returns False if itself or friend have empty inventory
    
    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
    
    # wave 6
    # add instance methods:
        # get_best_by_category
            # arg: str that represents a category
            # gets item with best condition in a certain category
            # returns this item (only a single item even if there are duplicates)
            # returns None if no matching items in inventory
        # swap_best_by_category
            # args: other - vendor instance, my_priority - category vendor wants, their_priority - category other wants
            # best item in my inventory that matches their_prority category is swapped with the best item in other's inventory that matches my priority
            # returns True
            # if vendor or other have no match, return False
    
    def get_best_by_category(self, category):
        get_same_category = self.get_by_category(category)
        if not get_same_category:
            best_item = None
        else:
            best_item = get_same_category[0]
            for item in get_same_category:
                if item.condition > best_item.condition:
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False
        else:
            self_best_item = self.get_best_by_category(their_priority)
            their_best_item = other.get_best_by_category(my_priority)
            self.swap_items(other, self_best_item, their_best_item)
            return True
    