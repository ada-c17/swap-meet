from .item import Item

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
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, vendor_to_swap_with, my_item, their_item):
        if my_item in self.inventory and their_item in vendor_to_swap_with.inventory:
            self.inventory.remove(my_item)
            vendor_to_swap_with.inventory.append(my_item)
            self.inventory.append(their_item)
            vendor_to_swap_with.inventory.remove(their_item)
            return True
        else:
            return False

