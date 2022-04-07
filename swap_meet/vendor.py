
class Vendor:

    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):
        try:
            self.inventory.remove(item)
        except(ValueError):
            return False
        return item

    def get_by_category(self, category_to_search):
        return_list = []
        for item in self.inventory:
            if item.category == category_to_search:
                return_list.append(item)
        return return_list

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.add(other_vendor.remove(their_item))
        other_vendor.add(self.remove(my_item))

        return True

    def swap_first_item(self, other_vendor):
        try:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        except IndexError:
            return False

        return True

    def get_best_by_category(self, desired_category):
        current_highest_rated = None
        for i in self.inventory:
            if i.category == desired_category:
                if not current_highest_rated:
                    current_highest_rated = i
                elif i.condition > current_highest_rated.condition:
                    current_highest_rated = i
        
        return current_highest_rated
        

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_highest_rated = self.get_best_by_category(their_priority)
        their_highest_rated = other.get_best_by_category(my_priority)
        if my_highest_rated and their_highest_rated:
            self.swap_items(other, my_highest_rated, their_highest_rated)
            return True
        else:
            return False