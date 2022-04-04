from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        """we can optionally pass in a list with the keyword argument inventory"""
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item
    
    #wave 2
    def get_by_category(self, category):
        same_category_items = []
        
        for i in self.inventory:
            if category == i.category:
                same_category_items.append(i)
            else:
                continue
        return same_category_items
    
    
    #wave 3
    def swap_items(self, o_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in o_vendor.inventory:
            return False
        
        if my_item in self.inventory:
            self.inventory.remove(my_item) #O(n)
            o_vendor.add(my_item) #O(1)
        if their_item in o_vendor.inventory:    
            o_vendor.remove(their_item) #O(n)
            self.inventory.append(their_item) #O(1)
        return True
       
    
    #wave 4
    def swap_first_item(self, o_vendor):
        if not self.inventory or not o_vendor.inventory:
            return False
    
        self.inventory[0], o_vendor.inventory[0] = o_vendor.inventory[0], self.inventory[0]
        return True
        
        
    
    