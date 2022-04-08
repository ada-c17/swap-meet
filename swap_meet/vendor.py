class Vendor:
    def __init__(self, inventory=None):
        # IMPORTANT BECAUSE LIST IS MUTABLE!!!
        # self.inventory = inventory
        # if self.inventory == None:
        #     self.inventory = []
        if inventory is None:
            inventory = []
        self.inventory = inventory
            
    def add(self, item):
        self.inventory.append(item)
        return item
            
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        inventory_list = []
        for item in self.inventory:
            if item.category == category:
                inventory_list.append(item)
        return inventory_list
        
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if len(self.inventory) and len(vendor.inventory) != 0:
            my_first_item = self.inventory[0]
            their_first_item = vendor.inventory[0]
            swap_first_items = self.swap_items(vendor, my_first_item, their_first_item)
            return swap_first_items
        
    def get_best_by_category(self, category):
        same_items = self.get_by_category(category)
        best_cond = None
        max_cond = 0
        for item in same_items:
            if item.condition > max_cond:
                max_cond = item.condition
                best_cond = item
        return best_cond
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        vendor_b_item = self.get_best_by_category(their_priority)
        other_b_item = other.get_best_by_category(my_priority)
        best_item_s = self.swap_items(other, vendor_b_item, other_b_item)
        return best_item_s
