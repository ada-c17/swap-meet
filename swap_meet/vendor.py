
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
    
    def swap_items(self, vendor_b, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_b.inventory:
            return False

        self.inventory.remove(my_item)
        vendor_b.inventory.remove(their_item)
        if their_item.category not in self.inventory:
            self.inventory.append(their_item)
            vendor_b.inventory.append(my_item)
        return True

    def swap_first_item(self, vendor_b):
        
        if not self.inventory or not vendor_b.inventory:
            return False
        
        self.inventory.append(vendor_b.inventory[0])
        vendor_b.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        vendor_b.inventory.remove(vendor_b.inventory[0])
            
        return True



