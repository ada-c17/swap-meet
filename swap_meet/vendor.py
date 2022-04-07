from .item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        # Initialize empty list that will hold all items of the correct category
        relevant_items = []
        # Iterate through inventory; if item is of correct category, add to list
        for item in self.inventory:
            if item.category == category:
                relevant_items.append(item)
        return relevant_items

    def swap(self, other_vendor, selfs_item, others_item):
        """Swaps two items between two vendors."""
        #remove self's item from self's inventory
        self.remove(selfs_item)
        #add self's item to other's inventory
        other_vendor.inventory.append(selfs_item)
        #remove other's item from other's inventory
        other_vendor.remove(others_item)
        #add other's item to self's inventory
        self.inventory.append(others_item)
        return True

    def swap_items(self, other_vendor, selfs_item, others_item):
        # Check items exist in respective inventories before attempting swap
        if selfs_item not in self.inventory or others_item not in other_vendor.inventory:
            print("You are trying to swap an item that either you or the other vendor does not have!")
            return False
        else:
            self.swap(other_vendor, selfs_item, others_item)
            return True

    def swap_first_item(self, other_vendor):
        # Check both vendors have items to swap, then swap them
        if self.inventory and other_vendor.inventory:
            self.swap(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        return False

    def get_best_by_category(self, category):
        highest_rating = 0.0
        best_item = None
        # Iterate through inventory items of correct category
        for item in self.inventory:
            if item.category == category:
        # If item's rating is higher than highest rating, reset
        # highest rated item to item, and highest rating to item's rating
                if item.condition > highest_rating:
                    highest_rating = item.condition
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
    # Check valid input
        if not self.inventory or not other.inventory:
            return False
    # Get best by category from self where category is other vendor's priority
        my_swap = self.get_best_by_category(their_priority)
    # Get best by category from other where category is my priority
        their_swap = other.get_best_by_category(my_priority)
    # Swap the two items 
        self.swap(other_vendor=other, selfs_item=my_swap, others_item=their_swap)
        return True
        

