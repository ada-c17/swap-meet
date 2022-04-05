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
### refactor this?? check first if any items match category??
        item_list = []
        for item in self.inventory:
            if item.category == category_string:
                item_list.append(item)
        return item_list
    
    def swap_items(self, Vendor, my_item, their_item):
        """Swaps items betwen self and another vendor's inventory"""
        # check valid input
        if my_item not in self.inventory or their_item not in Vendor.inventory:
            return False
        else:
            # remove items from inventory
            my_swap_item = self.remove(my_item)
            their_swap_item = Vendor.remove(their_item)
            # add items to new inventory 
            self.add(their_swap_item)
            Vendor.add(my_swap_item)
            return True
    
    def swap_first_item(self, Vendor):
        """Swaps first item in self and another vendor's inventory"""
        # check valid input
        if not self.inventory or not Vendor.inventory:
            return False
        else:
            my_first_item = self.inventory.pop(0)
            vendor_first_item = Vendor.inventory.pop(0)
            self.add(vendor_first_item)
            Vendor.add(my_first_item)
            return True
    
    def get_best_by_category(self, desired_category):
        """Returns item in best condition within a certain category"""
        # get list of items of category
        potential_items = self.get_by_category(desired_category)
        if not potential_items:
            return None
        elif len(potential_items) == 1:
            return potential_items[0]
        else:
            best_item = max(potential_items, key = lambda item: item.condition)
            return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swap best items in provided categories between self and another vendor"""
        pass