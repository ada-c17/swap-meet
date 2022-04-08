from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category_str):
        category_items = []
        for item in self.inventory:
            if item.category == category_str:
                category_items.append(item)
        return category_items

    def swap_items(self, swap_vendor, my_item, their_item):
        """
        - removes my_item from this Vendor's inventory, removes their_item from the other Vendor's inventory
        - returns True if both inventories have the respective items
        - returns False if one of the items is not contained in respective inventories
        """
        if my_item in self.inventory and their_item in swap_vendor.inventory:
            self.inventory.remove(my_item)
            swap_vendor.inventory.append(my_item)
            self.inventory.append(their_item)
            swap_vendor.inventory.remove(their_item)
            return True
        return False

    def swap_first_item(self, swap_vendor):
        """
        - removes the first item from its inventory, and adds the friend's first item
        - removes the first item from the friend's inventory, and adds the instances first item
        - returns True
        - either itself or the friend have an empty inventory, the method returns False
        """
        while len(self.inventory) >= 1 and len(swap_vendor.inventory) >= 1:
            self_first_item = self.inventory[0]
            swap_vendor_first_item = swap_vendor.inventory[0]

            self.inventory[0] = swap_vendor_first_item
            swap_vendor.inventory[0] = self_first_item
            return True
        return False

    def get_best_by_category(self, category_str):
        """get the item with the best condition in a certain category"""
        category_items = self.get_by_category(category_str)
        if len(category_items) > 1:
            best_item = category_items[0]
        else:
            return None

        for item in category_items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """swap the best item of certain categories with another Vendor
        my_priority = a category that the Vendor wants to receive
        their_priority = a category that the other wants to receive"""
        my_best_swap = self.get_best_by_category(their_priority)
        their_best_swap = other.get_best_by_category(my_priority)

        if my_best_swap and their_best_swap:
            self.swap_items(other, my_best_swap, their_best_swap)
            return True
        return False

    def get_newest_by_category(self, category_str):
        """optional enhancement: helper function to get newest item by category to pass to swap_by_newest"""
        category_items = self.get_by_category(category_str)
        if len(category_items) > 1:
            newest_item = category_items[0]
        else: 
            return None
        
        for item in category_items:
            if item.age < newest_item.age:
                newest_item = item
        
        return newest_item

    def swap_newest_by_category(self, other, my_priority, their_priority):
        """optional enhancement: swaps newest item of certain categories with another Vendor"""
        my_newest_swap = self.get_newest_by_category(their_priority)
        their_newest_swap = other.get_newest_by_category(my_priority)

        if my_newest_swap and their_newest_swap:
            self.swap_items(other, my_newest_swap, their_newest_swap)
            return True
        return False
