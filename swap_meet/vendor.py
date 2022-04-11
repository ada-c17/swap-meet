from email import message_from_binary_file


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.add(other_vendor.remove(their_item))
        other_vendor.add(self.remove(my_item))
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
        

    def get_best_by_category(self, category):
        max_condition = 0
        best_item = None
        items_by_category = self.get_by_category(category)
        for item in items_by_category:
            if item.condition > max_condition:
                max_condition = item.condition
                best_item = item

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best, their_best)

    def swap_by_newest(self, other):
        if not self.inventory or not other.inventory:
            return False

        my_items_with_known_ages = [item for item in self.inventory if item.age is not None]
        their_items_with_know_ages = [item for item in other.inventory if item.age is not None]

        if not my_items_with_known_ages or not their_items_with_know_ages:
            return False

        my_newest = my_items_with_known_ages[0]
        their_newest = their_items_with_know_ages[0]

        for item in my_items_with_known_ages:
            if item.age and item.age < my_newest.age:
                my_newest = item

        for item in their_items_with_know_ages:
            if item.age and item.age < their_newest.age:
                their_newest = item

        return self.swap_items(other, my_newest, their_newest)