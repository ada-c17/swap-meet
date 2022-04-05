from swap_meet.item import Item
from operator import attrgetter

class Vendor:

    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False    
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        categorized_items = []
        for item in self.inventory:
            if item.category == category:
                categorized_items.append(item)
        return categorized_items

    def swap_items(self, other_vendor, my_item, their_item):  
        if my_item not in self.inventory or \
            their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            return self.swap_items(other_vendor, my_first_item, their_first_item)

    def get_best_by_category(self, category):    
        if not self.get_by_category(category):
            return None
        return max(self.get_by_category(category), key=attrgetter("condition"))
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item, their_best_item)
        