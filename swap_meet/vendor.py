class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, item_given, item_received):
        if item_given not in self.inventory or item_received not in other.inventory:
            return False

        self.remove(item_given)
        self.add(item_received)
        other.remove(item_received)
        other.add(item_given)
        return True

    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False
        self.swap_items(other, self.inventory[0], other.inventory[0])
        return True

    def get_best_by_category(self, category):
        category_inventory = self.get_by_category(category)
        if len(category_inventory) < 1:
            return None
        best_item = category_inventory[0]
        for item in category_inventory:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        self.swap_items(other, my_best, their_best)
        return True
