class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
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

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            return True
    
    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.swap_items(vendor, my_item, their_item)
            return True

    def get_best_by_category(self, category):
        cat_items = self.get_by_category(category)
        highest_rating = 0.0
        best_item = None
        for item in cat_items:
            if item.condition > highest_rating:
                highest_rating = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if my_item and their_item:
            self.swap_items(other, my_item, their_item)
            return True
        return False