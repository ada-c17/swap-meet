class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
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

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.remove(my_item)
        self.add(their_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = vendor.inventory[0]

        self.swap_items(vendor, my_item, their_item)
        return True

    def get_best_by_category(self, category):
        matching_items = self.get_by_category(category)
        
        if not matching_items:
            return None

        matching_items.sort(key = lambda x: x.condition, reverse = True)
        return matching_items[0]

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False

        self.swap_items(other, my_item, their_item)
        return True