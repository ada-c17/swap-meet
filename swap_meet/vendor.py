class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory
        if self.inventory == None:
            self.inventory = []
    
    def add(self, item):
        if self.inventory == None:
            self.inventory = []
            self.inventory.append(item)
        else:
            self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        new_list = []
        for item in self.inventory:
            if item.category == category:
                new_list.append(item)
        return new_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.remove(their_item)
        else:
            return False
        vendor.add(my_item)
        self.add(their_item)
        return True

    def swap_first_item(self, vendor):
        if len(self.inventory) >=1 and len(vendor.inventory) >= 1:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        else:
            return False
        return True

    def get_best_by_category(self, category):
        max_condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition >= max_condition:
                    max_condition = item.condition
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        if my_item == None or their_item == None:
            return False
        self.swap_items(other, my_item, their_item)
        return True
