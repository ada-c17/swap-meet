from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)

        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False

    def get_by_category(self, category):
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            vendor.add(self.remove(my_item))
            self.add(vendor.remove(their_item))
            return True

        return False

    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            self.swap_items( vendor, self.inventory[0], vendor.inventory[0])
            return True
        return False

    def get_best_by_category(self, category):
        best_item = None
        best_condition = 0

        for item in self.get_by_category(category):
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if my_item in self.inventory and their_item in other.inventory:
            self.swap_items(other, my_item, their_item)
            return True
    
        return False

