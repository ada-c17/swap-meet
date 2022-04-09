class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

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
        filtered_items = []
        for item in self.inventory:
            if item.category == category:
                filtered_items.append(item)
        return filtered_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory:
            if their_item in vendor.inventory:
                self.remove(my_item)
                self.add(their_item)
                vendor.remove(their_item)
                vendor.add(my_item)
                return True
            else:
                return False
        else:
            return False

    def swap_first_item(self, vendor):
        try:
            self_first_item = self.inventory[0]
            vendor_first_item = vendor.inventory[0]
            self.swap_items(vendor, self_first_item, vendor_first_item)
            return True
        except IndexError:
            return False

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None
        else:
            best_rating = max(item.condition for item in items)
            for item in items:
                if item.condition is best_rating:
                    return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        self_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if their_best is None or self_best is None:
            return False
        else:
            self.swap_items(other, self_best, their_best)
            return True

    def get_newest_item(self):
        newest_age = min(item.age for item in self.inventory)
        for item in self.inventory:
            if item.age is newest_age:
                return item

    def swap_newest(self, other):
        self_newest_item = self.get_newest_item()
        their_newest_item = other.get_newest_item()
        self.swap_items(other, self_newest_item, their_newest_item)
