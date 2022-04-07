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
        category_items = []

        for item in self.inventory:
            if item.category == category:
                category_items.append(item)

        return category_items

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other_vendor.inventory.remove(their_item)
            other_vendor.inventory.append(my_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_item, their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        max_condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > max_condition:
                    max_condition = item.condition
                    best_item = item

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if my_best and their_best:
            self.swap_items(other, my_best, their_best)
            return True
        else:
            return False