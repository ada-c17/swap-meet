from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
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
        if my_item in self.inventory and their_item in swap_vendor.inventory:
            self.remove(my_item)
            swap_vendor.add(my_item)
            self.add(their_item)
            swap_vendor.remove(their_item)
            return True
        return False

    def swap_first_item(self, other):
        if len(self.inventory) >= 1 and len(other.inventory) >= 1:
            self_first_item = self.inventory[0]
            other_first_item = other.inventory[0]
            self.inventory[0] = other_first_item
            other.inventory[0] = self_first_item
            return True
        return False

    def get_best_by_category(self, category_str):
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
