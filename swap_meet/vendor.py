class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, new_item):
        if new_item in self.inventory:
            self.inventory.remove(new_item)
            return new_item
        return False
# WAVE 2
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result
    # WAVE 3
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True
        return False

    # WAVE 4
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_item, their_item)
            return True
        return False

    # WAVE 6
    def get_best_by_category(self, category):
        max = None
        max_condition = 0.0
        print(self.inventory)
        for item in self.inventory:
            if item.category == category and item.condition > max_condition:
                max = item
                max_condition = item.condition
        return max

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best:
            self.swap_items(other, my_best, their_best)
            return True
        return False
