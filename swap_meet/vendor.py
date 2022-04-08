
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
        items_matching_categories = []
        for item in self.inventory:
            if item.category == category:
                items_matching_categories.append(item)
        return items_matching_categories

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            friend.inventory.append(my_item)
            friend.inventory.remove(their_item)
            return True
        else:
            return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            if self.swap_items(friend, self.inventory[0], friend.inventory[0]):
                return True
        else:
            return False
        
    def get_best_by_category(self, category):
        items_in_category = [item for item in self.inventory if item.category == category]
        if len(items_in_category) == 0:
            return None
        
        best_condition_item = items_in_category[0]
        for item in items_in_category:
            if item.condition > best_condition_item.condition:
                best_condition_item = item

        return best_condition_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if self.get_best_by_category(their_priority) and other.get_best_by_category(my_priority):
            self.swap_items(other, self.get_best_by_category(their_priority), other.get_best_by_category(my_priority))
            return True
        else:
            return False


