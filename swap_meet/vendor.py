class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if self.inventory == None:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.remove(my_item)
            vendor.add(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            return True

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        else:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True

    def get_best_by_category(self, category):
        cat_items = self.get_by_category(category)
        items_conditions = [item.condition for item in cat_items]
        # if no item matched category ValueError will be raised during max()
        try:
            best_condition = max(items_conditions)
        except ValueError:
            return None

        for item in cat_items:
            if item.condition == best_condition:
                return item
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        for_me = other.get_best_by_category(my_priority)
        for_them = self.get_best_by_category(their_priority)
        if for_me and for_them:
            self.inventory.append(for_me)
            other.inventory.remove(for_me)
            other.inventory.append(for_them)
            self.inventory.remove(for_them)
        else:
            return False

        return True
