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
        
    #wave 6
    def get_best_by_category(self, category):
        same_category = self.get_by_category(category)
        if not same_category:
            return None
    
        conditions = [cond.condition for cond in same_category]
        highest_condition = max(conditions)
       
        for cond in same_category:
            if cond.condition >= highest_condition:
                return cond #should we return list contains multible?
            
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        other, which represents another Vendor instance to trade with
        my_priority, which represents a category that the Vendor wants to receive
        their_priority, which represents a category that other wants to receive
        """
        they_prefered, we_prefered = None, None
        for my_item in self.inventory:
            if their_priority == my_item.category:
                they_prefered = self.get_best_by_category(their_priority)
            else:
                continue
        for their_item in other.inventory:
            if my_priority != their_item.category:
                we_prefered = other.get_best_by_category(my_priority)
            else:
                continue
        
        return self.swap_items(other, they_prefered, we_prefered)