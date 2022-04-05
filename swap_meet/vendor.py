from swap_meet.item import Item
from operator import attrgetter

class Vendor:
    
    # constructor for class Vendor
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    # method to add item to inventory
    def add(self, item):
        self.inventory.append(item)
        return item
    
    # method to remove item from inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    # method to return list of items by item category
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    # method to swap from vendor's inventory to friend's inventory
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        return False

    # method to swap first item
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            # using swap_items method
            self.swap_items(other_vendor, my_item, their_item)
            return True
        return False

    # method to get item with best condition in a certain category
    def get_best_by_category(self, category):
        best_item_list = self.get_by_category(category)
        if best_item_list:
            return max(best_item_list, key=attrgetter("condition"))
        return None