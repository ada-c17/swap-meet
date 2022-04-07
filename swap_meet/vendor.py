class Vendor:
    '''Creating Vendor class that has an inventory attribute which is an optional argument. The add instance method adds a new item to inventory and the remove instance method
    removes an item if that item is found in the inventory list. If item is not found in list to remove, False is returned. '''
    def __init__(self, inventory=None): 
        if inventory is None: # shouldn't use mutable type as default parameter, so use None and then assign to empty list # O(1)
            inventory = [] 
        self.inventory = inventory 

    def add(self, item):
        self.inventory.append(item) # O(1)
        return item 
    
    def remove(self, item):
        if item in self.inventory: # O(1)
            self.inventory.remove(item) # O(1) 
            return item
        return False 

    def get_by_category(self, category):
        items_same_categories = [] 
        for item in self.inventory: # O(n)
            if item.category == category: # O(1)
                items_same_categories.append(item) # O(1)      
        return items_same_categories 

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            vendor.inventory.append(my_item)
            self.remove(my_item)
            vendor.inventory.remove(their_item)
            self.add(their_item)
            return True
        return False 
    
    def swap_first_item(self, vendor):
        if len(self.inventory) and len(vendor.inventory) != 0: 
            my_first_item = self.inventory[0]
            their_first_item = vendor.inventory[0]
            self.remove(my_first_item)
            vendor.inventory.append(my_first_item)
            vendor.inventory.remove(their_first_item)
            self.add(their_first_item)
            return True
        return False 
    
    def get_best_by_category(self, category):
        items_same_categories = self.get_by_category(category)
        item_best_condition = None
        max_condition = 0.0
        for item in items_same_categories:
            while item.condition > max_condition:
                max_condition = item.condition
                item_best_condition = item 
        return item_best_condition
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        vendor_best_item_by_category = self.get_best_by_category(their_priority)
        other_best_item_by_category = other.get_best_by_category(my_priority)
        best_swapped_items = self.swap_items(other, vendor_best_item_by_category, other_best_item_by_category)
        return best_swapped_items 




