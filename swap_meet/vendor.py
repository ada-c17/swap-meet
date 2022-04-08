from swap_meet.item import Item

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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True
        else:
            return False

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        else:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True

    def get_best_by_category(self, category=""):
        current_best_condition = 0
        best_item = None
        if self.get_by_category is None:
            return None
        for item in self.get_by_category(category):
            if item.condition > current_best_condition:
                current_best_condition = item.condition
                best_item = item
        return best_item
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        other_best = other.get_best_by_category(my_priority)
        vendor_best = self.get_best_by_category(their_priority)
        if not other_best or not vendor_best:
            return False
        else:
            return self.swap_items(other, vendor_best, other_best)
