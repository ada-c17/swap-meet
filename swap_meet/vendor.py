from .item import Item


class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False

    def get_by_category(self, category):
        result = [item for item in self.inventory if item.category is category]
        return result

    def get_best_by_category(self, category):
        all_by_category = self.get_by_category(category)

        if not all_by_category:
            return None

        max_rating = max(item.condition for item in all_by_category)
        best_by_category = [
            item for item in all_by_category if item.condition == max_rating
        ]
        # Assumed that in event of tie, return first item with highest rating
        return best_by_category[0]

    def swap_items(self, other_vendor, my_item, their_item):
        if not all([my_item in self.inventory, their_item in other_vendor.inventory]):
            return False

        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_they_want = self.get_best_by_category(their_priority)
        item_i_want = other.get_best_by_category(my_priority)

        # Checks if either .get_best_by returned False
        if not all([item_they_want, item_i_want]):
            return False

        return self.swap_items(other, item_they_want, item_i_want)

    def swap_first_item(self, other_vendor):
        if not all([self.inventory, other_vendor.inventory]):
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
