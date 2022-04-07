from swap_meet.item import Item
from operator import attrgetter

class Vendor:
    
    # constructor for class Vendor
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    # add item to inventory
    def add(self, item):
        self.inventory.append(item)
        return item
    
    # remove item from inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    # return list of items by item category
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    # swap from vendor's inventory to another vendor's inventory
    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            self.remove(my_item)
            self.add(their_item)
            other.remove(their_item)
            other.add(my_item)
            return True
        return False

    # swap vendor's first item in inventory with another vendor's first item
    def swap_first_item(self, other):
        if self.inventory and other.inventory:
            my_item = self.inventory[0]
            their_item = other.inventory[0]
            # using swap_items method
            self.swap_items(other, my_item, their_item)
            return True
        return False

    # get item with best condition in a certain category
    def get_best_by_category(self, category):
        # using get_by_category method
        best_item_list = self.get_by_category(category)
        if best_item_list:
            return max(best_item_list, key=attrgetter("condition"))
        return None

    # swap best item of certain categories with another vendor's best item
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority) # items from my inventory with their priority category
        their_best_item = other.get_best_by_category(my_priority) # items from their invenroy with my priority category
        return self.swap_items(other, my_best_item, their_best_item)

    # get item with best age (newest) in a certain category
    def get_newest_by_category(self, category):
        # using get_by_category method
        best_item_list = self.get_by_category(category)
        if best_item_list:
            return min(best_item_list, key=attrgetter("age"))
        return None

    # swap newest item of certain categories with another vendor's newest item
    def swap_by_newest(self, other, my_priority, their_priority):
        my_newest_item = self.get_newest_by_category(their_priority) # items from my inventory with their priority category
        their_newest_item = other.get_newest_by_category(my_priority) # items from their invenroy with my priority category
        print(my_newest_item)
        print(their_newest_item)
        print(self.inventory)
        return self.swap_items(other, my_newest_item, their_newest_item)