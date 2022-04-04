from operator import inv


class Vendor:
    def __init__(self, inventory= None):
        if not inventory:
            inventory = []
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
        list_items = []
        for item in self.inventory:
            if item.category == category:
                list_items.append(item)
        return list_items
    
    def swap_items(self, vendor,my_item,their_item):
        self.vendor = vendor
        self.my_item = my_item
        self.their_item = their_item
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
    
    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            temp_first_item = self.inventory[0]
            self.inventory[0] = vendor.inventory[0]
            vendor.inventory[0] = temp_first_item
            return True
        else:
            return False


