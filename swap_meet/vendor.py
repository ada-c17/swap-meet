from .item import Item
class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, new_item):
        """Add a new item to inventory"""

        self.inventory.append(new_item)
        return new_item
    
    def remove(self, discarded_item):
        """Remove an item from inventory"""

        if discarded_item not in self.inventory:
            return False
        else: 
            self.inventory.remove(discarded_item)
            return discarded_item
    
    def get_by_category(self, category_string):
        """Return list of items from inventory of a certain category"""

        item_list = []
        for item in self.inventory:
            if item.category == category_string:
                item_list.append(item)
        return item_list
    
    def swap_items(self, other, my_item, their_item):
        """Swaps items betwen self and another vendor's inventory"""

        # check valid input
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        else:
            # remove items from original inventory
            self.remove(my_item)
            other.remove(their_item)
            # add items to new inventory 
            self.add(their_item)
            other.add(my_item)
            return True
    
    def swap_first_item(self, Vendor):
        """Swaps first item in self and another vendor's inventory"""

        # check valid input
        if not self.inventory or not Vendor.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            vendor_first_item = Vendor.inventory[0]
            self.swap_items(Vendor, my_first_item, vendor_first_item)
            return True
    
    def get_best_by_category(self, desired_category):
        """Returns item in best condition within a certain category"""

        # get list of items of category
        potential_items = self.get_by_category(desired_category)
        # account for no items of desired category or only one of desired category
        if not potential_items:
            return None
        elif len(potential_items) == 1:
            return potential_items[0]
        # calculate max item condition
        else:
            best_item = max(potential_items, key = lambda item: item.condition)
            return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swap best items in provided categories between self and another vendor"""

        # get best items in each category
        their_desired_item = self.get_best_by_category(their_priority)
        my_desired_item = other.get_best_by_category(my_priority)

        # check validity
        if not my_desired_item or not their_desired_item:
            return False
        else:
            # swap items if valid
            return self.swap_items(other, their_desired_item, my_desired_item)
        

    def get_newest_item(self):
        """Returns newest item from inventory items with known ages"""

        potential_items = []
        for item in self.inventory:
            if item.age:
                potential_items.append(item)
        if not potential_items:
            return None
        elif len(potential_items) == 1:
            return potential_items[0]
        else:
            newest_item = min(potential_items, key = lambda item: item.age)
            return newest_item 
    
    def swap_by_newest(self, other):
        """Swaps newest items of self and another vendor"""

        their_newest = other.get_newest_item()
        my_newest = self.get_newest_item()

        if not my_newest or not their_newest:
            return False
        else:
            return self.swap_items(other, my_newest, their_newest)
