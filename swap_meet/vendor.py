class Vendor:

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        category_match = []
        for item in self.inventory:
            if item.category == category:
                category_match.append(item)
        return category_match

    def swap_items(self, Vendor, my_item, their_item):
        if my_item not in self.inventory  or their_item not in Vendor.inventory:
            return False
        self.add(their_item)
        Vendor.add(my_item)
        self.remove(my_item)
        Vendor.remove(their_item)
        return True

    def swap_first_item(self, Vendor):
        if not self.inventory or not Vendor.inventory:
            return False
        self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
        return True

    def get_best_by_category(self, category=""):
        condition = 0
        best_condition = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > condition:
                    condition = item.condition
                    best_condition = item
        return best_condition


    def swap_best_by_category(self, other, my_priority, their_priority):
        other_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if not other_best or not my_best:
            return False
        self.swap_items(other, my_best, other_best)
        return True
