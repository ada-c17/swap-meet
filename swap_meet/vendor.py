class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self,category):
        filtered_items = []
        for item in self.inventory:
            if item.category == category:
                filtered_items.append(item)
        return filtered_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory:
            if their_item in vendor.inventory:
                self.inventory.remove(my_item)
                self.inventory.append(their_item)
                vendor.inventory.remove(their_item)
                vendor.inventory.append(my_item)
                return True
            else:
                return False
        else: 
            return False
    
    def swap_first_item(self, vendor):
        try:
            self_first_item = self.inventory[0]
            vendor_first_item = vendor.inventory[0]
            self.inventory.remove(self_first_item)
            self.inventory.append(vendor_first_item)
            vendor.inventory.remove(vendor_first_item)
            vendor.inventory.append(self_first_item)
            return True
        except IndexError:
            return False
        

