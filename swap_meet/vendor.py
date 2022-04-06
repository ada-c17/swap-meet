class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
            
    def add(self, item):
        
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item == category:
                items_list.append(item)
        return items_list
    
    def swap_items(self, vendor, my_item, their_item):
            if my_item not in self.inventory or their_item not in vendor.inventory:
                return False
            self.remove(my_item)
            vendor.remove(their_item)
            vendor.add(my_item)
            self.add(their_item)
        
            return True
    
    def swap_first_item(self, vendor):
            if len(self.inventory) == 0 or len(vendor.inventory) == 0:
                return False
            my_item = self.inventory[0]
            friend_item = vendor.inventory[0]
            self.swap_items(vendor, my_item, friend_item)
            
            return True
    
    def get_best_by_category(self, category):
        best_condition = 0
        best_item = None
        for item in self.inventory:
            if 
        
        
        
    def swap_best_by_category(self, other, my_priority, their_prioirty):    
