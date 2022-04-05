class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            item_index = self.inventory.index(item)
            return self.inventory.pop(item_index)

    def get_by_category(self, category):
        # Returns a list of Items in the inventory with that category
        items_by_category = [item for item in self.inventory if item.category == category]
        return items_by_category
    
    def swap_items(self, vendor, my_item, their_item):
        if not self.remove(my_item):
            return False
        elif not vendor.remove(their_item):
            self.add(my_item)
            return False
        else:
            self.remove(my_item)
            vendor.add(my_item)

            vendor.remove(their_item)
            self.add(their_item)
            return True
    
    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if len(items_in_category) == 0:
            return None
        else:
            return max(items_in_category, key = lambda item: item.condition)
    # key = function where comparision of iterable is performed based on its return value

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        self.swap_items(other, my_best_item, their_best_item)
        return True