from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        """Adds an item to vendor's inventory."""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """Removes an item from Vendor's inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        """Retrieves all items from a vendor's inventory matching the given category."""
        # Initialize empty list that will hold all items of the correct category
        relevant_items = []
        # Iterate through inventory; if item is of correct category, add to list
        for item in self.inventory:
            if item.category == category:
                relevant_items.append(item)
        return relevant_items

    def swap(self, other_vendor, selfs_item, others_item):
        """Provides basic functionality for swapping two items between two vendors."""
        #remove self's item from self's inventory
        self.remove(selfs_item)
        #add self's item to other's inventory
        other_vendor.add(selfs_item)
        #remove other's item from other's inventory
        other_vendor.remove(others_item)
        #add other's item to self's inventory
        self.add(others_item)
        return True

    def swap_items(self, other_vendor, selfs_item, others_item):
        """Swaps two specific items between two vendors."""
        # Check items exist in respective inventories before attempting swap
        if selfs_item not in self.inventory or others_item not in other_vendor.inventory:
            print("You are trying to swap an item that either you or the other vendor does not have!")
            return False
        else:
            self.swap(other_vendor, selfs_item, others_item)
            return True

    def swap_first_item(self, other_vendor):
        """Swaps the first item in a vendor's inventory with the first in another vendor's inventory."""
        # Check both vendors have items to swap, then swap them
        if self.inventory and other_vendor.inventory:
            self.swap(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        return False

    def get_best_by_category(self, category):
        """Retrieves the item from a vendor's inventory of a certain category that is in the best condition."""
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
        """Swaps the items in best condition between two vendors of each vendor's preferred category."""
        # Check valid input
        if not self.inventory or not other.inventory:
            return False
        # Get best by category from self where category is other vendor's priority
        my_swap = self.get_best_by_category(their_priority)
        # Get best by category from other where category is my priority
        their_swap = other.get_best_by_category(my_priority)
        # If no item of desired category found, return False
        if not my_swap or not their_swap:
            return False
        # Swap the two items 
        self.swap(other_vendor=other, selfs_item=my_swap, others_item=their_swap)
        return True
        

